[Ransom Note](https://leetcode.com/problems/ransom-note)
```Python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for m in magazine:
            if m in ransomNote:
                ransomNote = ransomNote[:ransomNote.index(m)] + ransomNote[ransomNote.index(m)+1:]
        return not bool(ransomNote)
```