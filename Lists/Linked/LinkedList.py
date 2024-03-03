from Lists.Linked.Node import Node
import numpy as np


class LinkedList:
    def __init__(self) -> None:
        self.first = None

    def add(self, value):
        new_node = Node(value)
        # setando em o novo no (o no antigo)
        new_node.setNext(self.first)
        # o novo primeiro vai virar o novo que contem o no antigo
        self.first = new_node

    def print_list(self):
        current = self.first
        while current != None:
            print(current.print_node())
            current = current.getNext()

    def remove(self):
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.getNext()
        return temp

    def search(self, value):
        current = self.first
        while current.value != value:
            if current.getNext() == None:
                return None
            current = current.getNext()

        return current

    def remove_position(self, value):
        if not self.first:
            return None

        before = self.first
        current = self.first

        while current.value != value:
            if current.getNext() == None:
                return None
            before = current
            current = current.getNext()

        if self.first == current:
            self.first = self.first.getNext()
        else:
            before.setNext(current.getNext())
