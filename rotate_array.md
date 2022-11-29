[Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan&id=algorithm-i)

```Python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]
```