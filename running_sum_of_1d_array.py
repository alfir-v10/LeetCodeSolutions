"""
Given an array nums. We define a running sum of an array
    as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]
"""

from typing import List


class Solution:

    @staticmethod
    def running_sum_classic(nums: List[int]) -> List[int]:
        ret = []
        counter = 0
        i = 0
        for number in nums[i:]:
            counter += number
            i += 1
            ret.append(counter)
        return ret

    @staticmethod
    def running_sum_generator(nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
