import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from searching.binary_search import binary_search, search_insert_position


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_binary_search_empty():
    assert binary_search([], 1) == -1


def test_search_insert_position_middle():
    assert search_insert_position([1, 3, 5, 6], 5) == 2


def test_search_insert_position_end():
    assert search_insert_position([1, 3, 5, 6], 7) == 4


def test_search_insert_position_start():
    assert search_insert_position([1, 3, 5, 6], 0) == 0
