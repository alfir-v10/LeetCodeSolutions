[Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth)
```Python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
```