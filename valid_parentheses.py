"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution:

    @staticmethod
    def is_valid(self, s: str) -> bool:
        pair_parenth = {"(": ")", "[": "]",  "{": "}"}
        open_parenth = ["(", "[", "{"]
        stack = []
        for char in s:
            if char in open_parenth:
                stack.append(char)
            elif stack and char == pair_parenth[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []
