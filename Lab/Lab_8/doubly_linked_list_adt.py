# A Doubly Linked List abstract data type
#
# Written by Eric Martin for COMP9021


from copy import deepcopy


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    # Creates a linked list possibly from a list of values.
    def __init__(self, L=None, key=lambda x: x):
        self.key = key
        if L is None:
            self.head = None
            self.tail = None  # 一开始没给
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            self.tail = None  # 一开始没给
            return
        node = Node(L[0])
        self.head = node
        for e in L[1:]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node
        self.tail = node

    def print(self, separator=', '):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.print(separator = ' : ')
        2 : 0 : 1 : 3 : 7
        '''
        if not self.head:
            return
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.value))
            node = node.next_node
        print(separator.join(nodes))

    def duplicate(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL_copy = LL.duplicate()
        >>> LL_copy.print()
        2, 0, 1, 3, 7
        '''
        if not self.head:
            return
        node = self.head
        node_copy = Node(deepcopy(node.value))
        D = DoublyLinkedList(key=self.key)
        D.head = node_copy
        node = node.next_node
        while node:
            node_copy.next_node = Node(deepcopy(node.value))
            node_copy.next_node.previous_node = node_copy
            node_copy = node_copy.next_node
            node = node.next_node
        return D

    def length(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.length())
        5
        '''
        if not self.head:
            return 0
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next_node
        return length

    def apply_function(self, function):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.apply_function(lambda x: 2 * x)
        >>> LL.print()
        4, 0, 2, 6, 14
        '''
        node = self.head
        while node:
            node.value = function(node.value)
            node = node.next_node

    def is_sorted(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> print(LL.is_sorted())
        False
        '''
        node = self.head
        while node:
            # self.key  以key = lamba x 定义的排序
            if self.key(node.value) > self.key(node.next_node.value):
                return False
            else:
                node = node.next_node
        return True

    def extend(self, LL):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(LL.duplicate())
        >>> LL.print()
        2, 0, 1, 3, 7, 2, 0, 1, 3, 7
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7])
        >>> LL.extend(DoublyLinkedList([]))
        >>> LL.print()
        2, 0, 1, 3, 7
        '''

        if not LL.head:
            return
        if not self.head:
            self.head = LL.head
            # self.tail = LL.tail
            return
        self.tail.next_node = LL.head
        LL.head.previous_node = self.tail
        self.tail = LL.tail

    # ☆☆☆☆☆
    # tail = head， 第一个，然后把原来head后面的一个个重新连到head前面，作为新head....
    def reverse(self):
        '''
        >>> LL = DoublyLinkedList([2, 0, 1, 3, 7, 2, 0, 1, 3, 7])
        >>> LL.reverse()
        >>> LL.print()
        7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        if not self.head:
            return
        self.tail = self.head
        node = self.head.next_node
        self.head.next_node = None
        while node:
            next_node = node.next_node
            node.previous_node = None
            node.next_node = self.head
            self.head.previous_node = node
            self.head = node
            node = next_node


    def index_of_value(self, value):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.index_of_value(2))
        4
        >>> print(LL.index_of_value(5))
        -1
        '''
        node = self.head
        postion = 0
        while node:
            if node.value == value:
                return postion
            postion += 1
            node = node.next_node
        return -1

    def value_at(self, index):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> print(LL.value_at(4))
        2
        >>> print(LL.value_at(10))
        None
        '''
        node = self.head
        while index and node:
            index -= 1
            node = node.next_node
        if not node:
            return None
        return node.value

    def prepend(self, LL):
        '''
        >>> LL = DoublyLinkedList([7, 3, 1, 0, 2, 7, 3, 1, 0, 2])
        >>> LL.prepend(DoublyLinkedList([20, 21, 22]))
        >>> LL.print()
        20, 21, 22, 7, 3, 1, 0, 2, 7, 3, 1, 0, 2
        '''
        if not self.head:
            self.head = LL.head
            self.tail = LL.tail
        if not LL.head:
            return
        self.head.previous_node = LL.tail
        LL.tail.next_node = self.head
        self.head = LL.head

    def append(self, value):
        '''
        >>> LL = DoublyLinkedList()
        >>> LL.append(10)
        >>> LL.print()
        10
        >>> LL.append(15)
        >>> LL.print()
        10, 15
        '''
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            # 不是self.tail = Node(value) 一样还得next previous 连接一下
            return
        self.tail.next_node = Node(value)
        self.tail.next_node.previous_node = self.tail
        self.tail = self.tail.next_node

    def insert_value_at(self, value, index):
        '''
        >>> LL = DoublyLinkedList([10, 15])
        >>> LL.insert_value_at(5, 0)
        >>> LL.insert_value_at(25, 3)
        >>> LL.insert_value_at(20, 3)
        >>> LL.print()
        5, 10, 15, 20, 25
        '''
        new_node = Node(value)
        if index == 0:
            self.head.previous_node = new_node
            self.head.previous_node.next_node = self.head
            self.head = self.head.previous_node
            return
        node = self.head
        while index > 1 and node.next_node:
            index -= 1
            node = node.next_node
        tmp = node.next_node
        node.next_node = new_node
        new_node.previous_node = node
        if tmp:
            new_node.next_node = tmp
            tmp.previous_node = new_node
        else:
            self.tail = new_node

    # 在value_2前面插入value_1
    def insert_value_before(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([5, 10, 15, 20, 25])
        >>> LL.insert_value_before(0, 5)
        True
        >>> LL.insert_value_before(30, 35)
        False
        >>> LL.insert_value_before(22, 25)
        True
        >>> LL.insert_value_before(7, 10)
        True
        >>> LL.print()
        0, 5, 7, 10, 15, 20, 22, 25
        '''
        new_node = Node(value_1)
        if not self.head:
            return False
        node = self.head
        if node.value == value_2:
            self.head.previous_node = new_node
            self.head.previous_node.next_node = self.head
            self.head = self.head.previous_node
            return True
        while node:
            if node.value == value_2:
                tmp = node.previous_node
                node.previous_node = new_node
                new_node.next_node = node
                new_node.previous_node = tmp
                tmp.next_node = new_node
                return True
            node = node.next_node
        return False

    # 在value_2后面插入value_1
    def insert_value_after(self, value_1, value_2):
        '''
        >>> LL = DoublyLinkedList([0, 5, 7, 10, 15, 20, 22, 25])
        >>> LL.insert_value_after(3, 1)
        False
        >>> LL.insert_value_after(2, 0)
        True
        >>> LL.insert_value_after(12, 10)
        True
        >>> LL.insert_value_after(27, 25)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27

        '''
        new_node = Node(value_1)
        if self.tail.value == value_2:
            self.tail.next_node = new_node
            self.tail.next_node.previous_node = self.tail
            self.tail = new_node
            return True
        node = self.head
        while node:
            if node.value == value_2:
                tmp = node.next_node
                node.next_node = new_node
                new_node.previous_node = node
                if tmp:
                    new_node.next_node = tmp
                    tmp.previous_node = new_node
                return True
            node = node.next_node
        return False

    def insert_sorted_value(self, value):
        '''
        >>> LL = DoublyLinkedList([0, 2, 5, 7, 10, 12, 15, 20, 22, 25, 27])
        >>> LL.insert_sorted_value(-5)
        >>> LL.insert_sorted_value(17)
        >>> LL.insert_sorted_value(30)
        >>> LL.print()
        -5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30

        '''
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        if self.key(self.head.value) > self.key(value):
            self.head.previous_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node:
            if self.key(node.value) > self.key(value):
                tmp = node.previous_node
                node.previous_node = new_node
                new_node.next_node = node
                new_node.previous_node = tmp
                tmp.next_node = new_node
                return
            node = node.next_node
        self.tail.next_node = new_node
        new_node.previous_node = self.tail
        self.tail = new_node



    def delete_value(self, value):
        '''
        >>> LL = DoublyLinkedList([-5, 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30])
        >>> LL.delete_value(-5)
        True
        >>> LL.delete_value(30)
        True
        >>> LL.delete_value(15)
        True
        >>> LL.print()
        0, 2, 5, 7, 10, 12, 17, 20, 22, 25, 27

        '''
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next_node
            self.head.previous_node = None
            return True
        if self.tail.value == value:
            self.tail = self.tail.previous_node
            self.tail.next_node = None
            return True
        node = self.head
        while node:
            if node.value == value:
                node.previous_node.next_node = node.next_node
                return True
            node = node.next_node
        return False


if __name__ == '__main__':
    import doctest

    doctest.testmod()
