[Binary Search](https://leetcode.com/problems/binary-search/?envType=study-plan&id=algorithm-i)

###### My Solution
```Python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        if  target == nums[high]:
            return high
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
```
