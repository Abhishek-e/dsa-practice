import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from graphs.bfs_shortest_path import bfs_shortest_distances
from graphs.dijkstra import dijkstra


def test_bfs_shortest_distances():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    distances = bfs_shortest_distances(graph, "A")
    assert distances == {"A": 0, "B": 1, "C": 1, "D": 2}


def test_bfs_unreachable_node_excluded():
    graph = {"A": ["B"], "B": [], "C": []}
    distances = bfs_shortest_distances(graph, "A")
    assert "C" not in distances


def test_dijkstra_basic():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    distances = dijkstra(graph, "A")
    assert distances == {"A": 0, "B": 1, "C": 3, "D": 4}


def test_dijkstra_single_node():
    assert dijkstra({"A": []}, "A") == {"A": 0}
