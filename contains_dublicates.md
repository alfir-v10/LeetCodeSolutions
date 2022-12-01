[Contains Dublicates](https://leetcode.com/problems/contains-duplicate)

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return True
            d.update({num:i})
        return False
```

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

```Python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        i = 0
        while i < len(nums):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
            i += 1
        return False
```