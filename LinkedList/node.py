class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, o: object) -> bool:
        return self.data == o.data
