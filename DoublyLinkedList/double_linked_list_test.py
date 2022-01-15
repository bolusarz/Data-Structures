import unittest

from DoublyLinkedList.doubly_linked_list import DLinkedList


class DoubleLinkedListTestCase(unittest.TestCase):
    d_linked_list = None

    def setUp(self):
        self.d_linked_list = DLinkedList()

    def test_init(self):
        self.assertEqual(self.d_linked_list.head, None, "Head should be none")
        self.assertEqual(self.d_linked_list.get_size(), 0, "Size should be zero")

    def test_append_when_list_is_empty(self):
        self.d_linked_list.append(20)
        self.d_linked_list.append(45)
        self.assertEqual(self.d_linked_list.get_size(), 2, "size should be one")
        self.assertEqual(self.d_linked_list.head.data, 20, "head data should be 20")
        self.assertEqual(self.d_linked_list.head.next.data, 45, "next data should be 45")

    def test_insert(self):
        self.d_linked_list.insert(0, 25)
        self.d_linked_list.insert(0, 34)
        self.d_linked_list.insert(1, 48)
        self.assertEqual(self.d_linked_list.get_size(), 3, "size should be 3")
        self.assertEqual(self.d_linked_list.head.data, 34, "head data should be 34")
        self.assertEqual(self.d_linked_list.head.next.data, 48, "next data should be 48")
        self.assertEqual(self.d_linked_list.head.next.next.data, 25, "next data should be 25")

    def test_get(self):
        self.d_linked_list.insert(0, 25)
        self.d_linked_list.insert(0, 34)
        self.d_linked_list.append(20)
        self.d_linked_list.append(45)
        self.assertEqual(self.d_linked_list.get_size(), 4, "size should be 4")
        self.assertEqual(self.d_linked_list.get(0), 34, "head data should be 34")
        self.assertEqual(self.d_linked_list.get(1), 25, "next data should be 25")
        self.assertEqual(self.d_linked_list.get(2), 20, "next data should be 20")
        self.assertEqual(self.d_linked_list.get(3), 45, "next data should be 45")

    def test_get_exceptions(self):
        self.assertRaises(ValueError, self.d_linked_list.insert, -1, 12)
        self.assertRaises(ValueError, self.d_linked_list.insert, 1, None)

    def test_delete(self):
        self.d_linked_list.insert(0, 25)
        self.d_linked_list.insert(0, 34)
        self.d_linked_list.append(20)
        self.d_linked_list.append(45)

        self.d_linked_list.delete(25)
        self.assertEqual(self.d_linked_list.get_size(), 3, "size should be 3")
        self.assertEqual(self.d_linked_list.head.data, 34, "head data should be 34")

        self.d_linked_list.delete(45)
        self.assertEqual(self.d_linked_list.get_size(), 2, "size should be 2")
        self.assertEqual(self.d_linked_list.get(1), 20, "head data should be 20")


if __name__ == '__main__':
    unittest.main()
