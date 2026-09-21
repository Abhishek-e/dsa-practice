"""
BFS Shortest Path (unweighted graph)
--------------------------------------
Given an unweighted graph as an adjacency list and a start node, return the
shortest-path distance from `start` to every reachable node.

Approach: breadth-first search. BFS explores the graph in layers, so the
first time a node is reached is guaranteed to be via a shortest path (in
terms of edge count) when all edges have equal weight.

Time:  O(V + E)  -- every vertex and edge visited once
Space: O(V)      -- the distance map and the queue
"""
from collections import deque
from typing import Dict, List


def bfs_shortest_distances(graph: Dict[str, List[str]], start: str) -> Dict[str, int]:
    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    return distances
