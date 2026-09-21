import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from arrays.two_sum import two_sum
from arrays.kadane_max_subarray import max_subarray


def test_two_sum_finds_pair():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_not_adjacent():
    assert two_sum([3, 2, 4], 6) == (1, 2)


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 100) is None


def test_max_subarray_basic():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_all_negative():
    assert max_subarray([-3, -1, -4]) == -1


def test_max_subarray_single_element():
    assert max_subarray([5]) == 5
