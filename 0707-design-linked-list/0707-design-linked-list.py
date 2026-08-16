class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current is None:
                return -1
            current = current.next
        if current is None:
            return -1
        return current.val
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        previous = self.head
        for i in range(index - 1):
            previous = previous.next
        new_node.next = previous.next
        previous.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        previous = self.head
        for i in range(index - 1):
            if previous.next is None:
                return
            previous = previous.next
        if previous.next is None:
            return
        previous.next = previous.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)