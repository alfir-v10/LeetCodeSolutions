[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)
```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(map(int, bin(n)[2:]))
```

```Python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```