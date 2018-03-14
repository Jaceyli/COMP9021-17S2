
from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        if not self.head:
            return
        node = self.head
        while node:
            node1 = node
            while node1.next_node:
                if node.value == node1.next_node.value:
                    node1.next_node = node1.next_node.next_node
                else:
                    node1 = node1.next_node
            node = node.next_node






LL =  ExtendedLinkedList([1, 1, 2, 1, 2, 3, 3, 2, 1])
LL.remove_duplicates()
LL.print()