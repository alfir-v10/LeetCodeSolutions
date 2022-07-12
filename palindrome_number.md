[Palindrome Number](https://leetcode.com/problems/palindrome-number/)

###### My Solution
``` Python
class Solution(object):
    def number_len(self, x):
        x_len = 0
        while x:
            x = x // 10
            x_len += 1
        return x_len

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if self.number_len(x) == 1:
            return True
        x_tmp = x
        x_rev = 0
        while x_tmp:
            dig = x_tmp - x_tmp // 10 * 10
            x_rev += dig * pow(10, self.number_len(x_tmp) - 1)
            x_tmp = x_tmp // 10
            print(x_tmp, x_rev)
        if x - x_rev:
            return False
        return True
```
###### Best Practice
``` Python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x /= 10
        return x == revertedNumber or x == revertedNumber / 10
```