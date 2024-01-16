[Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike)
```Python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = len(s) // 2
        count_a = 0
        count_b = 0

        for v in s[:half]:
            if v in 'aeiou':
                count_a += 1

        for v in s[half:]:
            if v in 'aeiou':
                count_b += 1
        return count_a == count_b
```

```Python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s) % 2:
            half = len(s) // 2 + 1
        else:
            half = len(s) // 2 
        a = s[:half]
        b = s[half:]
        if self.count_vowels(a) == self.count_vowels(b):
            return True
        return False
        
    def count_vowels(self, s: str):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for v in s.lower():
            if v in vowels:
                count += 1
        return count
```