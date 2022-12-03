[Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero)
```Python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num:
            if not num % 2:
                num /= 2
            else:
                num -= 1
            i += 1
        return i
```

```Python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while num:
            if not num & 1:
                num >>= 1
            else:
                num -= 1
            i += 1
        return i
```