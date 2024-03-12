class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def print_node(self):
        print(self.value)
