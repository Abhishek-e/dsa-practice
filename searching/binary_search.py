"""
Binary Search
-------------
Given a sorted array `nums` and a target value, return its index, or -1 if
not present.

Approach: repeatedly halve the search window by comparing the target to the
middle element.

Time:  O(log n)
Space: O(1) iterative
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_insert_position(nums: List[int], target: int) -> int:
    """Where `target` would be inserted to keep `nums` sorted (bisect_left)."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
