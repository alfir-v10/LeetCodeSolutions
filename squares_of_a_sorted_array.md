[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/?envType=study-plan&id=algorithm-i)
```Python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums) - 1
        res = [0] * len(nums)
        j = len(res) - 1
        while low <= high:
            if abs(nums[low]) < abs(nums[high]):
                res[j] = nums[high] ** 2
                high -= 1
                j -= 1
            else:
                res[j] = nums[low] ** 2
                low += 1
                j -= 1
        return res
```