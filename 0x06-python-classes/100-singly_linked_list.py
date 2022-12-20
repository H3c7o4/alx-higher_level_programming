#!/usr/bin/python3
"""
Node class: defines a node of a singly linked list
"""


class Node:
    """class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialize attributes

        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data of the current node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the value of the data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Return the data of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node

        Args:
            data (int): the value of the node
            next_node (Node): the next Node
        """
        if type(value) is Node or Value is None:
            self.__next_node = Value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class that defines a singly linked list"""
    def __init__(self):
        """Initialize attributes"""
        self.__head = None

    def __str__(self):
        """sets the print behavior for the singly linked list object"""
        sll_str = ""
        node = self.__head
        if node is not None:
            sll_str += str(node.data) + '\n'
            node = node.next_node
        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head
        if node is None or self.__head.data >= value:
            self.__head = Node(Value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
