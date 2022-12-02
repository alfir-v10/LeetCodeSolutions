[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists)

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        p1 = list1
        p2 = list2

        p3 = None
        if p1.val <= p2.val:
            p3 = p1
            p1 = p1.next
        elif p1.val > p2.val:
            p3 = p2
            p2 = p2.next
        p3_head = p3

        while p1 or p2:
            if p1 is None:
                while p2:
                    p3.next = p2
                    p3 = p3.next
                    p2 = p2.next
                return p3_head
            elif p2 is None:
                while p1:
                    p3.next = p1
                    p3 = p3.next
                    p1 = p1.next
                return p3_head

            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
            elif p1.val > p2.val:
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
            else:
                p3.next = p1
                p1 = p1.next
                p3 = p3.next
                p3.next = p2
                p2 = p2.next
                p3 = p3.next
        return p3_head
```

```Python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```