from LinkedList.node import Node


class LinkedList:
    """
    An implementation of the abstract data type LinkedList
    Supports insertion, deletion
    """

    def __init__(self, data=None):
        if data:
            self.head = self.__create_node__(data)
        else:
            self.head = None
        self.size = int(self.head is not None)

    def get(self, index: int):
        """
        Returns the Node value at the given index
        :param index: position of the Node object
        :return: Node object
        """
        current = self.head
        position = self.__resolve_index(index)
        if position >= self.size:
            raise IndexError("list index out of range")
        for _ in range(0, position):
            current = current.next
        return current.data

    def append(self, data):
        """
        Adds a new node to the end of the linked list
        :param data: the value of the node to be appended
        :return: Nothing
        """
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
        """
        Inserts a new node at a given index

        Example:
            Given a linkedlist => 2 -> 3 -> 5 ->
            Inserting 10 at index 2 would be => 2 -> 3 -> 10 -> 5 ->

        Note: To insert item at the end of the list, use append method.

        If index given is larger than the size of the linked list, the
        new node is appended to the end of the list.


        :param index: The position for the new node to be inserted
        :param data: The value of the new node tobe inserted
        :return: Nothing
        """
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
                for i in range(0, position - 1):
                    current = current.next
                node.next = current.next
                current.next = node
        else:
            self.head = node
        self.size += 1

    def delete(self, index):
        """
        Deletes a node at the supplied index

        :param index: The position of the node to be deleted
        :return: Nothing
        :raise: IndexError
        """
        current = self.head
        position = self.__resolve_index(index)
        if position >= self.size:
            raise IndexError('list index out of bounds')
        if position == 0:
            self.head = None
            self.size = 0
        else:
            for _ in range(0, position - 1):
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def __getitem__(self, item):
        """
        Returns the value stored in the node at a given index

        :param item: The index of the node whose value is to be returned
        :return: The value of the selected node
        """
        return self.get(item)

    def __setitem__(self, key, value):
        """
        Changes the value stored in a node at a given index

        :param key(int): The index of the node to be modified
        :param value: The new value of the node
        :return: Nothing
        """
        current = self.head
        position = self.__resolve_index(key)
        if position >= self.size:
            raise IndexError("list index out of bounds")
        for _ in range(0, position):
            current = current.next
        current.data = value

    def __str__(self):
        """
        :return: A string representation of Linked List
        """
        list_str = ""
        current = self.head
        while current:
            list_str += f"{current.data} -> "
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

    def __resolve_index(self, index) -> int:
        """
        Returns an absolute value of the index used for accessing items in the linked list

        Example:
            arr = [1,2,3,4]
            arr[-1] is meant to return the last item in the list
            the index -1 is transformed into the last index which is 3

        :param index (int): The index to be accessed to be negative

        :return: The actual index in the linked list
        """

        if index < 0:
            return abs(self.size + index)
        return index
