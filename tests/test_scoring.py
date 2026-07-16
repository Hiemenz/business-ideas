"""Tests for scoring logic in gemini_client."""
import pytest
from gemini_client import _clean_scores, parse_json_block, composite_score, SCORE_KEYS


class TestCleanScores:
    def test_valid_list(self):
        raw = [{"market_size": 7, "feasibility": 8, "novelty": 6, "competition": 5}]
        result = _clean_scores(raw, 1)
        assert len(result) == 1
        assert result[0]["market_size"] == 7.0

    def test_coerces_ints_to_float(self):
        raw = [{"market_size": 7, "feasibility": 8, "novelty": 6, "competition": 5}]
        result = _clean_scores(raw, 1)
        assert all(isinstance(result[0][k], float) for k in SCORE_KEYS)

    def test_bad_entry_becomes_none(self):
        raw = [{"market_size": "bad", "feasibility": 8, "novelty": 6, "competition": 5}]
        result = _clean_scores(raw, 1)
        assert result[0] is None

    def test_missing_key_becomes_none(self):
        raw = [{"market_size": 7, "feasibility": 8}]
        result = _clean_scores(raw, 1)
        assert result[0] is None

    def test_pads_short_list(self):
        result = _clean_scores([], 3)
        assert result == [None, None, None]

    def test_truncates_long_list(self):
        entry = {"market_size": 7, "feasibility": 8, "novelty": 6, "competition": 5}
        result = _clean_scores([entry] * 5, 2)
        assert len(result) == 2

    def test_non_list_returns_nones(self):
        result = _clean_scores("oops", 2)
        assert result == [None, None]


class TestParseJsonBlock:
    def test_bare_object(self):
        assert parse_json_block('{"a": 1}') == {"a": 1}

    def test_bare_array(self):
        assert parse_json_block('[1, 2, 3]') == [1, 2, 3]

    def test_strips_markdown_fence(self):
        raw = "```json\n{\"a\": 1}\n```"
        assert parse_json_block(raw) == {"a": 1}

    def test_extracts_from_surrounding_text(self):
        raw = 'Here is the result: {"score": 9} — enjoy!'
        assert parse_json_block(raw) == {"score": 9}

    def test_raises_on_no_json(self):
        with pytest.raises(ValueError):
            parse_json_block("no json here at all")


class TestCompositeScore:
    def test_average_of_four(self):
        score = {"market_size": 8.0, "feasibility": 6.0, "novelty": 7.0, "competition": 5.0}
        assert composite_score(score) == 6.5

    def test_rounds_to_one_decimal(self):
        score = {"market_size": 7.0, "feasibility": 8.0, "novelty": 6.0, "competition": 6.0}
        result = composite_score(score)
        assert result == round(result, 1)
