class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        count = 0
        if index < 0 or index >= self.size:
            return -1

        tmp = self.head
        while count < index:
            count += 1
            tmp = tmp.next
        return tmp.value

        """"
    def addAtHead(self, val: int) -> None:

    def addAtTail(self, val: int) -> None:

    def addAtIndex(self, index: int, val: int) -> None:

    def deleteAtIndex(self, index: int) -> None:
"""

