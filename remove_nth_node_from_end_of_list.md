[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)
```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_save = head
        len_list = 0
        while head:
            len_list += 1
            head = head.next
        cut_node = len_list - n
        prev_node = None
        i = 0
        head = head_save
        while i < cut_node and head:
            prev_node = head
            head = head.next
            i += 1
        if prev_node is None and head.next is None:
            return None
        elif prev_node is None and head.next:
            return head.next
        elif prev_node and head.next is None:
            prev_node.next = None
            return head_save
        else:
            prev_node.next = head.next
            return head_save
```