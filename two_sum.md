[Two Sum](https://leetcode.com/problems/two-sum/)

###### My Solutions
``` Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        for i, k in enumerate(nums):
            next_find = target - k
            try:
                tmp = nums[i+1:]
                idx = tmp.index(next_find) + (i+1)
            except ValueError:
                pass
            if idx:
                return [i, idx]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(nums) - 1
        nums_sorted = sorted(nums, reverse=False)
        while left_idx < right_idx:
            current_sum = nums_sorted[left_idx] + nums_sorted[right_idx]
            if current_sum == target:
                if nums.index(nums_sorted[left_idx]) == nums.index(nums_sorted[right_idx]):
                    print(nums[nums.index(nums_sorted[left_idx])+1:])
                    return [nums.index(nums_sorted[left_idx]), nums[nums.index(nums_sorted[left_idx])+1:].index(nums_sorted[right_idx]) + nums.index(nums_sorted[left_idx])+1]
                return [nums.index(nums_sorted[left_idx]), nums.index(nums_sorted[right_idx])]
            elif current_sum < target:
                left_idx += 1
            else:
                right_idx -= 1


```
###### Best Practice
``` Python
class Solution: 
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		checker = {}
		for i, val in enumerate(nums): 
			if (target - val) in checker:
				return [checker[(target - val)],i] 
			checker[val] = i 
		return
```
