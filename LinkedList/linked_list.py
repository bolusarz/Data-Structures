from LinkedList.node import Node


class LinkedList:

    def __init__(self, data=None):
        if data:
            self.head = self.__create_node__(data)
        else:
            self.head = None
        self.size = int(self.head is not None)

    def get(self, index: int):
        current = self.head
        position = self.__resolve_index(index)
        if position >= self.size:
            raise IndexError("list index out of range")
        for _ in range(0, position):
            current = current.next
        return current.data

    def append(self, data):
        current = self.head
        node = self.__create_node__(data)
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.size += 1

    def insert(self, index, data):
        current = self.head
        node = self.__create_node__(data)
        position = self.__resolve_index(index)
        if position > self.size:
            position = self.size
        if current:
            if index == 0:
                node.next = self.head.next
                self.head = node
            else:
                for i in range(0, position-1):
                    current = current.next
                node.next = current.next
                current.next = node
        else:
            self.head = node
        self.size += 1

    def delete(self, index):
        current = self.head
        position = self.__resolve_index(index)
        if position >= self.size:
            raise IndexError('list index out of bounds')
        if position == 0:
            self.head = None
            self.size = 0
        else:
            for _ in range(0, position-1):
                current = current.next
            current.next = current.next.next
            self.size -= 1


    @staticmethod
    def __create_node__(data):
        return Node(data)

    def __resolve_index(self, index) -> int:
        if index < 0:
            return abs(self.size + index)
        return index

