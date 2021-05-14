"""
Partitioning Into Minimum Number Of Deci-Binary Numbers
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
 For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary
numbers needed so that they sum up to n.
Example 1:
    Input: n = "32"
    Output: 3
    Explanation: 10 + 11 + 11 = 32
Example 2:
    Input: n = "82734"
    Output: 8
Example 3:
    Input: n = "27346209830709182346"
    Output: 9
"""


class Solution:
    @staticmethod
    def min_partitions(n: str) -> int:
        min_count = -pow(10, 19)
        for c in n:
            if int(c) > min_count:
                min_count = int(c)
        return min_count
