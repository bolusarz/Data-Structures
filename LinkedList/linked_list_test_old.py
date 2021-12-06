import unittest

from LinkedList.node import Node
from LinkedList.linkedlistOld import LinkedList


class LinkedListCreationTestCase(unittest.TestCase):
    def test_creation_without_node(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)

    def test_creation_with_node(self):
        linked_list = LinkedList(Node(2))
        self.assertEqual(linked_list.head, Node(2))


class LinkedListInsertionTestCase(unittest.TestCase):

    def test_insert_at_head(self):
        linked_list = LinkedList(Node(2))
        linked_list.insert_first(Node(4))
        self.assertEqual(linked_list.head, Node(4))

    def test_append(self):
        linked_list = LinkedList(Node(5))
        linked_list.append(Node(7))
        linked_list.append(Node(1))
        linked_list.append(Node(2))
        self.assertEqual(linked_list.get_last(), Node(2))

    def test_append_when_list_is_empty(self):
        linked_list = LinkedList()
        linked_list.append(Node(5))
        self.assertEqual(linked_list.size(), 1)

    def test_size_of_empty_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.size(), 0)

    def test_size(self):
        linked_list = LinkedList()
        linked_list.append(Node(7))
        linked_list.append(Node(1))
        linked_list.append(Node(2))
        self.assertEqual(linked_list.size(), 3)


class LinkedListAccessTestCase(unittest.TestCase):

    def test_get_first(self):
        linked_list = LinkedList(Node(2))
        self.assertEqual(linked_list.get_first(), Node(2))

    def test_get_last(self):
        linked_list = LinkedList(Node(3))
        linked_list.append(Node(7))
        linked_list.append(Node(1))
        linked_list.append(Node(2))
        self.assertEqual(linked_list.get_last(), Node(2))

    def test_get_at(self):
        linked_list = LinkedList(Node(3))
        linked_list.append(Node(7))
        linked_list.append(Node(1))
        linked_list.append(Node(2))
        self.assertEqual(linked_list.get_at(1), Node(7))

    def test_get_at_invalid_index(self):
        linked_list = LinkedList(Node(3))
        self.assertIsNone(linked_list.get_at(20))


if __name__ == '__main__':
    unittest.main()
