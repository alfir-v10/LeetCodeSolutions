[First Bad Version](https://leetcode.com/problems/first-bad-version/description/?envType=study-plan&id=algorithm-i)

###### My Solution
```Python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            elif not isBadVersion(mid):
                low = mid + 1
        return high
```