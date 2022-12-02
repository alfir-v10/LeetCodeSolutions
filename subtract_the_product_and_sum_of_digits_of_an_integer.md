[Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer)
```Python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = [*map(int, list(str(n)))]
        prod = 1
        for num in numbers:
            prod *= num
        return prod - sum(numbers)
```