"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.
Example 3:
    Input: nums = [1,2,3]
    Output: 0
"""
from typing import List


class Solution:
    @staticmethod
    def num_identical_pairs(nums: List[int]) -> int:
        count_pairs = 0
        i = 0
        for num in nums[i:]:
            i += 1
            for nbr in nums[i:]:
                if num == nbr:
                    count_pairs += 1
        return count_pairs
