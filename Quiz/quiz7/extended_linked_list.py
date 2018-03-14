# Written by JINGXUAN LI for COMP9021

from linked_list_adt import *


class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        even1 = True
        last_even = 0
        odd1 = True
        node1 = self.head
        while node1:
            if node1.value % 2 != 0:
                even1 = False
            else:
                last_even = node1.value
                odd1 = False
            node1 = node1.next_node
        if even1: #all even
            return
        if odd1:  #all odd
            return

        node = self.head
        while node.value % 2 == 0:
            while node.next_node:
                node = node.next_node
            tmp = self.head
            self.head = self.head.next_node
            tmp.next_node = None
            node.next_node = tmp
            node = self.head

        current_node = self.head
        while current_node.next_node:
            # if odd :next
            if current_node.next_node.value % 2 != 0:
                current_node = current_node.next_node
                continue
            #check finish: if last node is last even
            node_tmp = current_node
            while node_tmp.next_node:
                node_tmp = node_tmp.next_node
            if node_tmp.value == last_even:
                return
            # if even :cut it and link it to the last one
            if current_node.next_node.value % 2 == 0:
                tmp = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                tmp.next_node = None
                node2 = current_node
                while node2.next_node:
                    node2 = node2.next_node
                node2.next_node = tmp

            # self.print()