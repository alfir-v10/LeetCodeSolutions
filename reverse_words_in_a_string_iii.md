[Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii)
```Python
class Solution:
    def reverseWord(self, s: str) -> str:
        return ''.join(list(s)[::-1])

    def reverseWords(self, s: str) -> str:
        return ' '.join([self.reverseWord(w) for w in s.split(' ')])
```

```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split(' ')])
```
