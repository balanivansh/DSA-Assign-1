class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtIndex(self, index, value):
        if index < 0:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        if self.head is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        current.next = current.next.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head is None

    def rotateRight(self, k):
        if not self.head or k == 0:
            return
        length = self.size()
        k = k % length
        if k == 0:
            return
        slow, fast = self.head, self.head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = self.head
        self.head = new_head

    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head

    def interleave(self, other_list):
        dummy = Node()
        tail = dummy
        l1, l2 = self.head, other_list.head
        while l1 or l2:
            if l1:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            if l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        self.head = dummy.next

    def getMiddle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def indexOf(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def splitAtIndex(self, index):
        if index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            self.head = None
            return new_list
        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        new_list = SinglyLinkedList()
        new_list.head = current.next
        current.next = None
        return new_list
