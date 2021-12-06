import unittest

# Create empty linked list
# Create linked list with an initial value
# Check the size of the linked list
# Add item to the back of a linked list
# Add item at a given position in a linked list
# Remove an item at a given position in the linked list
# Return an item at a given index
from LinkedList.linked_list import LinkedList


class LinkedListCreationTestCase(unittest.TestCase):
    def test_create_linked_list_with_empty_data(self):
        my_list = LinkedList()
        self.assertEqual(my_list.size, 0)

    def test_create_linked_list_with_data(self):
        my_list = LinkedList(2)
        self.assertEqual(my_list.size, 1)


class LinkedListAccessTestCase(unittest.TestCase):

    def test_get_item_linked_list(self):
        my_list = LinkedList(5)
        self.assertEqual(my_list[0], 5)

    def test_get_item_at_negative_index(self):
        my_list = LinkedList(5)
        my_list.append(3)
        my_list.append(30)
        self.assertEqual(my_list.get(-1), 30)

    def test_get_item_does_not_exist_linked_list(self):
        my_list = LinkedList()
        with self.assertRaises(IndexError):
            my_list.get(3)


class LinkedListInsertionTestCase(unittest.TestCase):

    def test_append_when_list_is_empty(self):
        my_list = LinkedList()
        my_list.append(2)
        self.assertEqual(my_list.get(0), 2)

    def test_append_when_list_is_not_empty(self):
        my_list = LinkedList(5)
        my_list.append(2)
        my_list.append(1)
        my_list.append(4)
        self.assertEqual(my_list.get(-1), 4)

    def test_insert_when_list_size_less_than_index(self):
        my_list = LinkedList(2)
        my_list.append(3)
        my_list.insert(4, 10)
        self.assertEqual(my_list.get(-1), 10)

    def test_insert_when_list_size_greater_than_index(self):
        my_list = LinkedList(4)
        my_list.append(3)
        my_list.append(30)
        my_list.append(2)
        my_list[2] = 25
        self.assertEqual(my_list.get(2), 25)

    def test_insert_at_head(self):
        my_list = LinkedList(10)
        my_list.insert(0, 15)
        self.assertEqual(my_list.get(0), 15)


class LinkedListDeletionTestCase(unittest.TestCase):

    def test_delete_head(self):
        my_list = LinkedList(20)
        my_list.delete(0)
        self.assertEqual(my_list.size, 0)

    def test_delete_tail(self):
        my_list = LinkedList(4)
        my_list.append(3)
        my_list.append(30)
        my_list.delete(-1)
        self.assertEqual(my_list.get(-1), 3)

    def test_delete_between(self):
        my_list = LinkedList(4)
        my_list.append(3)
        my_list.append(30)
        my_list.delete(1)
        self.assertEqual(my_list.get(1), 30)

    def test_delete_invalid_index(self):
        my_list = LinkedList(4)
        my_list.append(3)
        my_list.append(30)
        with self.assertRaises(IndexError):
            my_list.delete(20)


if __name__ == '__main__':
    unittest.main()
