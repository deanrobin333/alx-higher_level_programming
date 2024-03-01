#!/usr/bin/python3
'''singly linked list'''


class Node:
    '''class that defines a node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''initiates a node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''creates data from private instance'''
        return self.__data

    @data.setter
    def data(self, value):
        '''modifies private data safely'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        ''' creates next node private instance'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    '''Represents a singl-linked list'''

    def __init__(self):
        '''Initialize a new singly linked list'''
        self.__head = None

    def sorted_insert(self, value):
        '''
        Inserts a new Node into the correct sorted position in the list,
        (increasing order)

        Args:
            value (Node): The new Node to insert of type Node
        '''

        new = Node(value)  # create a new instance of Node class
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            '''insert new node just before head'''
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            '''
            - while stops when the `tmp.next_node.data`
              is greater than `tmp.data`
            - hence we insert `new` node between `tmp` and `tmp.next_node`.
            '''
            while (
                    tmp.next_node is not None and
                    tmp.next_node.data < value
                    ):
                tmp = tmp.next_node
            '''
            - inserting between tmp and tmp.next_node
            - new.next_node must point to `tmp.next_node` and then
              new becomes `tmp.next_node`
            '''
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        '''should print entire list when __str__ is called'''
        list_values = []
        tmp = self.__head
        while tmp is not None:
            list_values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(list_values))
