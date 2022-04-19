[Two Sum](https://leetcode.com/problems/two-sum/)

###### My Solution
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
