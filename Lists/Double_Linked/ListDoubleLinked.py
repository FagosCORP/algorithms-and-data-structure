from Lists.Double_Linked.Node import Node


class ListDoubleLinked:
    def __init__(self) -> None:
        self.first = None
        self.last = None

    def __is_empty(self) -> bool:
        return not self.first

    def add_first(self, value):
        new_first = Node(value)
        if self.__is_empty():
            self.last = new_first

        new_first.setNext(self.first)
        self.first = new_first

    def add_last(self, value):
        new_last = Node(value)
        if self.__is_empty():
            self.first = new_last
        else:
            self.last.setNext(new_last)
        self.last = new_last

    def print_list(self):
        if self.__is_empty():
            exit("List is empty")
        current = self.first
        while current != None:
            current.print_node()
            current = current.getNext()


listLinkedDouble = ListDoubleLinked()
listLinkedDouble.add_first(5)
listLinkedDouble.add_first(4)
listLinkedDouble.add_first(3)
