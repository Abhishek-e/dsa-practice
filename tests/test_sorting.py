import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sorting.merge_sort import merge_sort


def test_merge_sort_unsorted():
    assert merge_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_merge_sort_already_sorted():
    assert merge_sort([1, 2, 3]) == [1, 2, 3]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_duplicates():
    assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_merge_sort_does_not_mutate_input():
    original = [3, 1, 2]
    merge_sort(original)
    assert original == [3, 1, 2]
