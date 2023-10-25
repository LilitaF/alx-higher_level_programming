#!/usr/bin/python3
"""define a class node"""
class Node:
    """Represent class node"""
    def __init__(self, data, next_node=None):
        """initialise the node"""
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """set the data"""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """get or set the next node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represent the new linked list"""
    def __init__(self):
        """insert new node"""
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """define the print representation of the singly linked list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return ("\n".join(map(str, result)))

