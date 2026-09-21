"""
Dijkstra's Algorithm (single-source shortest path, non-negative weights)
--------------------------------------------------------------------------
Given a weighted graph as an adjacency list {node: [(neighbor, weight), ...]}
and a start node, return the shortest distance from `start` to every
reachable node.

Approach: greedily expand the closest unvisited node using a min-heap,
relaxing its neighbors' distances. Requires non-negative edge weights.

Time:  O((V + E) log V)  -- each edge relaxation is a heap push, O(log V)
Space: O(V)              -- distance map and heap
"""
import heapq
from typing import Dict, List, Tuple


def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str) -> Dict[str, int]:
    distances = {start: 0}
    heap = [(0, start)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances
