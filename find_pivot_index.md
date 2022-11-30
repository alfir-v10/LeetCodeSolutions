[Find Pivot Index](https://leetcode.com/problems/find-pivot-index)
```Python
#Time Limit Exceeded
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i+1]) == sum(nums[i:]):
                return i
        return -1
```

```Python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        i = 0
        total_sum = sum(nums)
        while i < len(nums):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
            i += 1
        return -1
```

```Python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i, v in enumerate(nums):
            left_sum += v
            if left_sum == right_sum:
                return i
            right_sum -= v
        return -1
```