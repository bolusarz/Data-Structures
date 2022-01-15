from DoublyLinkedList.node import Node


class DLinkedList:

    def __init__(self, data=None):
        if data:
            self.head = self.__create_node__(data)
        else:
            self.head = None
        self.__size = int(self.head is not None)

    def get_size(self):
        return self.__size

    def insert(self, index, data):

        if data is None:
            raise ValueError("Data can not be none")

        if index < 0:
            raise ValueError("Index can not be a negative number")

        node = self.__create_node__(data)
        current = self.head

        if not self.head:
            self.head = node

        elif index == 0:
            node.next = current
            current.prev = node
            self.head = node

        elif index >= self.__size:
            self.append(data)

        else:
            while index > 0:
                current = current.next
                index -= 1
            node.next, node.prev = current, current.prev
            current.prev.next = node

        self.__size += 1

    def get(self, index):
        current = self.head

        if index > self.__size:
            raise IndexError("index is larger than list size")

        while index > 0:
            current = current.next
            index -= 1

        return current.data

    def append(self, data):
        node = self.__create_node__(data)

        if not self.head:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node
            node.prev = current

        self.__size += 1

    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:
                break
            current = current.next

        if current:
            if not current.prev:
                self.head, self.head.prev = current.next, None
            else:
                if current.next:
                    current.prev.next, current.next.prev = current.next, current.prev
                else:
                    current.prev.next = None
            self.__size -= 1
        return current

    def __str__(self):
        current = self.head
        list_str = ""
        while current:
            list_str += f"{current.data} "
            current = current.next
        return list_str

    @staticmethod
    def __create_node__(data):
        """
        A helper method that create Node objects

        :param data:
        :return: A Node object
        """
        return Node(data)
