[Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram)
```Python
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t_hash = {a: t.count(a) for a in set(t)}
        cnt_dict = {}
        for k, v in {a: s.count(a) for a in set(s)}.items():
            if k in t_hash and v == t_hash[k]:
                continue
            else:
                if k not in t_hash:
                    cnt_dict[k] = v
                elif v > t_hash[k]:
                    cnt_dict[k] = v - t_hash[k]
                else:
                    continue
        return sum(cnt_dict.values())
        
```