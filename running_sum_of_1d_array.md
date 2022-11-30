[Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array)

```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 1
        len_nums = len(nums)
        while i < len_nums:
            nums[i] = nums[i] + nums[i-1]
            i += 1
        return nums
```
```Python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
```