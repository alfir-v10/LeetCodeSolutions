"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
from typing import List


class Solution:

    @staticmethod
    def max_sub_array(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray