"""
Maximum Subarray (Kadane's Algorithm)
--------------------------------------
Given an integer array `nums`, find the contiguous subarray with the largest
sum and return that sum.

Approach: at each position, decide whether to extend the running subarray or
start a new one there (`current = max(num, current + num)`), and track the
best sum seen so far. This is a classic 1-D dynamic programming problem
solved in constant extra space.

Time:  O(n)  -- single pass
Space: O(1)  -- two running variables
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    best = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best
