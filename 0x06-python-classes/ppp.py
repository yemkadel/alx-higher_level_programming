#!/usr/bin/python3

""" The file create singly linked list in python """


class Node:
    """ This is a Node class """

    @property
    def data(self):
        """ getter method for Node data """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter method for Node data """
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """ getter method for next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter method for next node """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    
    """ This is a singlylinkedList Class """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ this function inserts a new node into a linked list in a sorted way """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node.data < value and temp.next_node is not None):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """ defines the __str__ property of this class """
        val = []
        temp = self.__head
        while (temp is not None):
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))

