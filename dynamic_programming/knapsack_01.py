"""
0/1 Knapsack
------------
Given item weights, item values, and a capacity, find the maximum total
value achievable without exceeding the weight capacity. Each item can be
taken at most once (hence "0/1").

Approach: bottom-up DP over (item index, remaining capacity). Space is
optimized to a single 1-D array by iterating capacity in reverse, since each
item may only be used once.

Time:  O(n * capacity)
Space: O(capacity)
"""
from typing import List


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    if len(weights) != len(values):
        raise ValueError("weights and values must be the same length")

    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)

    return dp[capacity]
