[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)
```Python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        min_len = min(list(map(len, strs)))
        hash_prefix_table = {}
        words = [word[:min_len] for word in strs]
        for word in words:
            i = 0
            while i < min_len + 1:
                if word[:i] not in hash_prefix_table:
                    hash_prefix_table.update({word[:i]: 1})
                else:
                    hash_prefix_table[word[:i]] += 1
                i += 1
        max_pref = 0
        pref = ''
        for key in hash_prefix_table:
            if len(key) > max_pref and hash_prefix_table[key] == strs_len:
                max_pref = len(key)
                pref = key
        return pref
```