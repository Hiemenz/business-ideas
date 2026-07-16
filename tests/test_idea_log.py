"""Tests for idea_log schema migration."""
import pandas as pd
from idea_log import load_log, DEFAULTS, STATUSES


class TestLoadLog:
    def test_missing_file_returns_empty_df(self, tmp_path):
        df = load_log(path=tmp_path / "nonexistent.parquet")
        assert df.empty
        assert set(DEFAULTS.keys()).issubset(set(df.columns))

    def test_missing_columns_backfilled(self, tmp_path):
        """A parquet written without newer columns gets them on load."""
        path = tmp_path / "log.parquet"
        minimal = pd.DataFrame([{"idea": "test idea", "hash": "abc123"}])
        minimal.to_parquet(path, index=False)

        df = load_log(path=path)
        for col, default in DEFAULTS.items():
            assert col in df.columns

    def test_existing_data_preserved(self, tmp_path):
        path = tmp_path / "log.parquet"
        original = pd.DataFrame([{
            "idea": "my idea", "hash": "abc", "score": 7.5,
            "industry": "fintech", "business_model": "saas",
            **{k: v for k, v in DEFAULTS.items() if k not in ("idea", "hash", "score", "industry", "business_model")},
        }])
        original.to_parquet(path, index=False)

        df = load_log(path=path)
        assert df.loc[0, "score"] == 7.5
        assert df.loc[0, "idea"] == "my idea"


class TestStatuses:
    def test_lifecycle_order(self):
        expected = ["generated", "unscored", "onepager", "poc", "launched", "killed"]
        assert STATUSES == expected
