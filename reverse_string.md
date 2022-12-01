[Reverse String](https://leetcode.com/problems/reverse-string)

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
```

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -=1
```

```Python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for i in range(len_s// 2):
            s[i], s[len_s-i-1] = s[len_s-i-1], s[i]
```