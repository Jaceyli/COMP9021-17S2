
from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            node = current_node
            while node.next_node:
                if current_node.value == node.next_node.value:
                    node.next_node = node.next_node.next_node
                else:
                    node = node.next_node
            current_node = current_node.next_node


LL =  ExtendedLinkedList([1, 1, 2, 1, 2, 3, 3, 2, 1])
LL.remove_duplicates()
LL.print()



