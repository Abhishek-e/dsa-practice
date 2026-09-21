"""
Two Sum
-------
Given an array of integers `nums` and a target `t`, return the indices of the
two numbers that add up to `t`. Assumes exactly one valid answer exists and
each element is used once.

Approach: single pass with a hash map of value -> index. For each number,
check whether its complement (t - num) has already been seen.

Time:  O(n)  -- one pass, O(1) average dict lookups
Space: O(n)  -- the hash map, worst case holds n-1 elements
"""
from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None
