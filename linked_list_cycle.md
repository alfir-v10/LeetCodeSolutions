[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_p = head
        fast_p = head
        while (slow_p and slow_p.next) and (fast_p and fast_p.next):
            fast_p = fast_p.next
            if slow_p is fast_p:
                return True
            fast_p = fast_p.next
            slow_p = slow_p.next
        return False
```
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
```