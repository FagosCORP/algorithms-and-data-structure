class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.before = None
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setBefore(self, before):
        self.before = before

    def getBefore(self):
        return self.before

    def print_node(self):
        print(self.value)
