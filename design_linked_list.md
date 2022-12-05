[Design Linked List](https://leetcode.com/problems/design-linked-list)
```Python
class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        ptr = self.head
        if index >= self.len:
            return -1
        while index > 0 and ptr and ptr.next:
            ptr = ptr.next
            index -= 1
        return ptr.val if ptr else -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            self.len += 1
            return
        self.head.prev = ListNode(val)
        self.head.prev.next = self.head
        self.head = self.head.prev
        self.len += 1

    def addAtTail(self, val: int) -> None:
        ptr = self.head
        if ptr is None:
            self.head = ListNode(val)
            self.len += 1
            return
        while ptr and ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(val, prev=ptr)
        ptr.next.prev = ptr
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        ptr = self.head
        if self.len < index:
            return
        if ptr is None or index == self.len:
            self.addAtTail(val)
            return
        while index > 0 and ptr and ptr.next:
            ptr = ptr.next
            index -= 1
        node = ListNode(val)
        if (ptr.next is None and ptr.prev) or (ptr.next and ptr.prev):
            node.prev = ptr.prev
            node.next = ptr
            ptr.prev.next = node
            ptr.prev = node
            self.len += 1
        if (ptr.next and ptr.prev is None) or (ptr.next is None and ptr.prev is None):
            self.addAtHead(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.len <= index or self.head is None:
            return
        ptr = self.head
        while index > 0 and ptr and ptr.next:
            ptr = ptr.next
            index -= 1
        if ptr.next is None and ptr.prev is None:
            self.head = None
        elif ptr.next is None and ptr.prev:
            ptr.prev.next = None
            ptr.prev = None
        elif ptr.next and ptr.prev is None:
            ptr.next.prev = None
            self.head = ptr.next
            ptr.next = None
        else:
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev
            ptr.next = None
            ptr.prev = None
        self.len -= 1

    def printList(self) -> None:
        ptr = self.head
        s = []
        if ptr:
            s.append(ptr.val)
        while ptr and ptr.next:
            ptr = ptr.next
            s.append(ptr.val)
        print(s)
```