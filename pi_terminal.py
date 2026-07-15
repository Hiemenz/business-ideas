"""Manages long-lived interactive `claude` terminal sessions spawned via a pty.

Each Discord user gets at most one session, backed by a real pseudo-terminal
so the Claude Code CLI runs exactly as it would in an interactive shell.
Output is streamed back through an `on_output` callback the caller supplies
(kept decoupled from Discord so this module has no bot-specific imports).
"""

import asyncio
import os
import pty
import re
import signal

ANSI_RE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
FLUSH_DELAY_SECONDS = 0.6
READ_CHUNK_BYTES = 4096


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text).replace("\r", "")


class TerminalSession:
    def __init__(self, loop, command, cwd, on_output, on_exit=None):
        self.loop = loop
        self.on_output = on_output
        self.on_exit = on_exit

        self.master_fd, slave_fd = pty.openpty()
        self.pid = os.fork()
        if self.pid == 0:
            # Child: attach to the pty slave and exec the command.
            os.close(self.master_fd)
            os.setsid()
            os.dup2(slave_fd, 0)
            os.dup2(slave_fd, 1)
            os.dup2(slave_fd, 2)
            os.close(slave_fd)
            if cwd:
                os.chdir(cwd)
            env = dict(os.environ)
            env.setdefault("TERM", "xterm-256color")
            try:
                os.execvpe(command[0], command, env)
            finally:
                os._exit(1)

        os.close(slave_fd)
        self._buffer = bytearray()
        self._flush_task = None
        self._alive = True
        self.loop.add_reader(self.master_fd, self._on_readable)

    def _on_readable(self):
        try:
            data = os.read(self.master_fd, READ_CHUNK_BYTES)
        except OSError:
            data = b""
        if not data:
            self._teardown(exited=True)
            return
        self._buffer.extend(data)
        if self._flush_task is None or self._flush_task.done():
            self._flush_task = self.loop.create_task(self._flush_soon())

    async def _flush_soon(self):
        await asyncio.sleep(FLUSH_DELAY_SECONDS)
        if not self._buffer:
            return
        text = strip_ansi(self._buffer.decode("utf-8", errors="replace"))
        self._buffer.clear()
        if text.strip():
            await self.on_output(text)

    def write(self, text: str):
        if not self._alive:
            raise RuntimeError("session is not running")
        os.write(self.master_fd, text.encode() + b"\n")

    def clear_context(self):
        """Send Claude Code's built-in /clear — resets context, keeps the process alive."""
        self.write("/clear")

    def _teardown(self, exited=False):
        if not self._alive:
            return
        self._alive = False
        try:
            self.loop.remove_reader(self.master_fd)
        except Exception:
            pass
        try:
            os.close(self.master_fd)
        except OSError:
            pass
        if exited and self.on_exit:
            self.loop.create_task(self.on_exit())

    def stop(self):
        if not self._alive:
            return
        try:
            os.killpg(self.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        self._teardown()

    @property
    def alive(self):
        return self._alive


class TerminalManager:
    """One session per user_id. Caller is responsible for authorization checks."""

    def __init__(self, command, cwd=None):
        self.command = command
        self.cwd = cwd
        self._sessions: dict[int, TerminalSession] = {}

    def has_session(self, user_id: int) -> bool:
        return user_id in self._sessions and self._sessions[user_id].alive

    def start(self, user_id: int, on_output) -> TerminalSession:
        if self.has_session(user_id):
            raise RuntimeError("session already running")

        loop = asyncio.get_running_loop()

        async def on_exit():
            self._sessions.pop(user_id, None)
            await on_output("_[session ended]_")

        session = TerminalSession(loop, self.command, self.cwd, on_output, on_exit=on_exit)
        self._sessions[user_id] = session
        return session

    def get(self, user_id: int) -> TerminalSession | None:
        return self._sessions.get(user_id)

    def send(self, user_id: int, text: str):
        session = self.get(user_id)
        if not session or not session.alive:
            raise RuntimeError("no active session")
        session.write(text)

    def clear(self, user_id: int):
        session = self.get(user_id)
        if not session or not session.alive:
            raise RuntimeError("no active session")
        session.clear_context()

    def stop(self, user_id: int):
        session = self._sessions.pop(user_id, None)
        if session:
            session.stop()
