class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.prev = left
        self.next = right
