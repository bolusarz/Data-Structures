from .node import Node


class LinkedList:

    def __init__(self, first=None):
        self.head: Node = first

    def size(self):
        current = self.head
        n = 0
        while current:
            current = current.next
            n += 1
        return n

    def insert_first(self, node: Node):
        node.next = self.head
        self.head = node

    def append(self, node: Node):
        current: Node = self.head
        if not current:
            self.head = node
        else:
            while current.next:
                current = current.next
            current.next = node

    def insert_after(self, node: Node):
        current: Node = self.head
        while current and current.data != node.data:
            current = current.next
        node.next = current.next
        current.next = node

    def get_first(self) -> Node:
        return self.head

    def get_last(self) -> Node:
        current: Node = self.head
        while current.next:
            current = current.next
        return current

    def get_at(self, index: int):
        current: Node = self.head
        i = 0
        if index == 0:
            return self.head
        while current and i < index:
            current = current.next
            i += 1
        return current
