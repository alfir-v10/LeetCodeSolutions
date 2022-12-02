[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        len_list = 0
        while head:
            len_list += 1
            head = head.next
        mid_node = len_list // 2 + 1
        while mid_node-1:
            mid_node -= 1
            tmp = tmp.next
        return tmp
```

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        while p1:
            p1 = p1.next
            if p1:
                p1 = p1.next
                p2 = p2.next
        return p2
```
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        for _ in range(n):
            p1=p1.next
        if not p1:
            return p2.next
        while p1.next:
            p2=p2.next
            p1=p1.next
        p2.next=p2.next.next
        return head
```