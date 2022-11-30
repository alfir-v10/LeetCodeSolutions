[Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
```Python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {v:i for i,v in enumerate(s)}
        t_dict = {v:i for i,v in enumerate(t)}
        new_s = ''.join([str(s_dict[i]) for i in s])
        new_t = ''.join([str(t_dict[i]) for i in t])
        if new_s == new_t:
            return True
        return False
```

```Python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.index, s)) == list(map(t.index, t)) if len(s) == len(t) else False
```