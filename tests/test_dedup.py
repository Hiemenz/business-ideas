"""Tests for embedding dedup logic."""
import json
import numpy as np
import pytest


def cosine_sim(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def is_duplicate_fn(embedding, stored_embeddings, model="gemini-embedding-001", threshold=0.85):
    """Extracted logic from main.is_duplicate for unit testing."""
    dim = len(embedding)
    stored_vecs = [
        v["vec"] for v in stored_embeddings.values()
        if isinstance(v, dict) and v.get("model") == model and len(v.get("vec", [])) == dim
    ]
    if not stored_vecs:
        return False
    stored_vecs = np.array(stored_vecs)
    vec = np.array(embedding)
    sims = (stored_vecs @ vec) / (np.linalg.norm(stored_vecs, axis=1) * np.linalg.norm(vec))
    return float(sims.max()) > threshold


class TestIsDuplicate:
    def test_identical_is_duplicate(self):
        vec = [1.0, 0.0, 0.0]
        store = {"abc": {"model": "gemini-embedding-001", "vec": vec}}
        assert is_duplicate_fn(vec, store) is True

    def test_orthogonal_is_not_duplicate(self):
        store = {"abc": {"model": "gemini-embedding-001", "vec": [1.0, 0.0, 0.0]}}
        assert is_duplicate_fn([0.0, 1.0, 0.0], store) is False

    def test_empty_store_never_duplicate(self):
        assert is_duplicate_fn([1.0, 0.0], {}) is False

    def test_different_model_ignored(self):
        store = {"abc": {"model": "other-model", "vec": [1.0, 0.0, 0.0]}}
        assert is_duplicate_fn([1.0, 0.0, 0.0], store) is False

    def test_dimension_mismatch_ignored(self):
        store = {"abc": {"model": "gemini-embedding-001", "vec": [1.0, 0.0, 0.0]}}
        assert is_duplicate_fn([1.0, 0.0], store) is False

    def test_near_duplicate_above_threshold(self):
        base = [1.0, 0.1, 0.0]
        near = [1.0, 0.09, 0.0]
        store = {"abc": {"model": "gemini-embedding-001", "vec": base}}
        assert is_duplicate_fn(near, store, threshold=0.85) is True

    def test_below_threshold_not_duplicate(self):
        store = {"abc": {"model": "gemini-embedding-001", "vec": [1.0, 0.0, 0.0]}}
        assert is_duplicate_fn([0.5, 0.866, 0.0], store, threshold=0.85) is False


class TestEmbeddingsSerialization:
    def test_roundtrip_json(self):
        data = {
            "key1": {"model": "gemini-embedding-001", "vec": [0.1, 0.2, 0.3]},
        }
        serialized = json.dumps(data)
        restored = json.loads(serialized)
        assert restored["key1"]["vec"] == pytest.approx([0.1, 0.2, 0.3])
