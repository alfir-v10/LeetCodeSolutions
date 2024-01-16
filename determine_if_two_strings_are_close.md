[Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close)
```Python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        hash1 = sorted({k: word1.count(k) for k in set(word1)}.values())
        hash2 = sorted({k: word2.count(k) for k in set(word2)}.values())
        return hash1 == hash2
```