import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dynamic_programming.longest_common_subsequence import lcs_length
from dynamic_programming.knapsack_01 import knapsack_01


def test_lcs_basic():
    assert lcs_length("abcde", "ace") == 3


def test_lcs_no_common():
    assert lcs_length("abc", "xyz") == 0


def test_lcs_identical():
    assert lcs_length("abc", "abc") == 3


def test_knapsack_basic():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    assert knapsack_01(weights, values, 7) == 9


def test_knapsack_zero_capacity():
    assert knapsack_01([1, 2], [10, 20], 0) == 0


def test_knapsack_mismatched_lengths_raises():
    try:
        knapsack_01([1, 2], [10], 5)
        assert False, "expected ValueError"
    except ValueError:
        pass
