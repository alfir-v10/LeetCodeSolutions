[Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range)
```Python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high - low == 1:
            return 1
        if low % 2 != 0 and high % 2 != 0:
            return (high - low + 1) - (high - low) // 2
        elif low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1
```

```Python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
```