[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_p = head
        fast_p = head
        while (slow_p and slow_p.next) and (fast_p and fast_p.next):
            fast_p = fast_p.next
            if slow_p is fast_p:
                ptr = head
                fast_p = fast_p.next
                while ptr != fast_p:
                    ptr = ptr.next
                    fast_p = fast_p.next
                return ptr
            fast_p = fast_p.next
            slow_p = slow_p.next
        return None
```