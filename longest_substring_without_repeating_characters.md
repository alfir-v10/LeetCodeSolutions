[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
```Python

```
```Python
# First Run - Time Limit Exceeded
class Solution:
    def has_dublicate(self, s):
        return len(s) != len(set(s))

    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = len(s) - 1
        flag = 0
        while low != high:
            i = 0
            j = high
            max_len = 0
            while j < len(s):
                window_sub = s[i: j + 1]
                if not self.has_dublicate(window_sub):
                    if max_len <= len(window_sub):
                        max_len = len(window_sub)
                    flag = 1
                i += 1
                j += 1
            if flag:
                return max_len
            high -= 1
        return 1
```

```Python
# Second Run - Success
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if not s_len:
            return 0
        i = 0
        j = s_len - 1
        max_len = 0
        while i <= j:
            k = i
            substring = set()
            while k <= j and s[k] not in substring:
                substring.add(s[k])
                k += 1
            len_sub = k - i
            max_len = max(max_len, len_sub)
            i += 1
        return max_len
```