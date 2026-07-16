"""Tests for validation scoring logic."""
import math
from validate import compute_validation


class TestComputeValidation:
    def test_both_sources_available(self):
        reddit = {"count": 5, "engagement": 500, "titles": ["title"]}
        hn     = {"total": 20, "points": 300, "titles": ["hn"], "competitors": 2}
        score, summary = compute_validation(reddit, hn)
        assert 0 <= score <= 10
        assert "Reddit" in summary
        assert "HN" in summary

    def test_reddit_unavailable_normalizes(self):
        hn = {"total": 50, "points": 1000, "titles": [], "competitors": 1}
        score, summary = compute_validation(None, hn)
        assert 0 <= score <= 10
        assert "not counted" in summary

    def test_hn_unavailable_normalizes(self):
        reddit = {"count": 8, "engagement": 1000, "titles": []}
        score, summary = compute_validation(reddit, None)
        assert 0 <= score <= 10

    def test_both_unavailable_returns_nan(self):
        score, summary = compute_validation(None, None)
        assert math.isnan(score)

    def test_competition_sweet_spot(self):
        """1-3 competitors = validated market = max competition points."""
        hn_sweet = {"total": 10, "points": 100, "titles": [], "competitors": 2}
        hn_none  = {"total": 10, "points": 100, "titles": [], "competitors": 0}
        hn_crowded = {"total": 10, "points": 100, "titles": [], "competitors": 5}
        reddit = {"count": 0, "engagement": 0, "titles": []}

        s_sweet,   _ = compute_validation(reddit, hn_sweet)
        s_none,    _ = compute_validation(reddit, hn_none)
        s_crowded, _ = compute_validation(reddit, hn_crowded)

        assert s_sweet > s_none
        assert s_sweet > s_crowded

    def test_score_caps_at_10(self):
        reddit = {"count": 100, "engagement": 99999, "titles": []}
        hn     = {"total": 9999, "points": 99999, "titles": [], "competitors": 2}
        score, _ = compute_validation(reddit, hn)
        assert score <= 10
