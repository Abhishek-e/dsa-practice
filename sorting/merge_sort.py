"""
Merge Sort
----------
Classic divide-and-conquer, stable, comparison sort.

Approach: recursively split the array in half, sort each half, then merge
the two sorted halves in linear time.

Time:  O(n log n) in all cases
Space: O(n) for the merge buffers
"""
from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
