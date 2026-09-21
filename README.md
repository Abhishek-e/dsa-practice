# DSA Practice

Solved algorithm and data-structure problems in Python, each with a short
written explanation of the approach and its time/space complexity, backed
by a passing test suite — not just links to LeetCode.

## Why this repo exists

Most of my other repos are full applications (a CRM, an LMS, a data
analyzer). This one isolates the algorithms/DSA fundamentals on their own,
with reasoning made explicit rather than buried in application code.

## Structure

```
dsa-practice/
├── arrays/                  # two-pointer / hashing / Kadane's
├── searching/                # binary search family
├── sorting/                   # merge sort
├── graphs/                    # BFS, Dijkstra
├── dynamic_programming/       # LCS, 0/1 knapsack
└── tests/                     # pytest suite, one file per category
```

## Problems covered

| Problem | Category | Technique | Time | Space |
| --- | --- | --- | --- | --- |
| Two Sum | Arrays | Hash map | O(n) | O(n) |
| Maximum Subarray | Arrays | Kadane's algorithm (1-D DP) | O(n) | O(1) |
| Binary Search + Insert Position | Searching | Divide and conquer | O(log n) | O(1) |
| Merge Sort | Sorting | Divide and conquer | O(n log n) | O(n) |
| BFS Shortest Path | Graphs | Breadth-first search | O(V + E) | O(V) |
| Dijkstra's Algorithm | Graphs | Greedy + min-heap | O((V+E) log V) | O(V) |
| Longest Common Subsequence | Dynamic Programming | Bottom-up DP | O(m·n) | O(m·n) |
| 0/1 Knapsack | Dynamic Programming | Bottom-up DP, space-optimized | O(n·cap) | O(cap) |

Each solution file's docstring states the problem, the approach, and why
that time/space complexity holds — read the code, not just the table.

## Run the tests

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 -m pytest -v
```

27 tests, all passing.
