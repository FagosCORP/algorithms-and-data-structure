from Lists.Linked.Node import Node
import numpy as np


class LinkedList:
    def __init__(self) -> None:
        self.first = None

    def add(self, value):
        novo = Node(value)
        # setando em o novo no (o no antigo)
        novo.setNext(self.first)
        # o novo primeiro vai virar o novo que contem o no antigo
        self.first = novo

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
            if current.value == None:
                exit("Value is not finded.")

            current = current.getNext()

        return current
