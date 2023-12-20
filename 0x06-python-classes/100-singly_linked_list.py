#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        tmp = self.__head
        datas = []
        while tmp is not None:
            datas.append("{:d}".format(tmp.data))
            tmp = tmp.next_node
        return "\n".join(datas)

    def sorted_insert(self, value):
        tmp = self.__head
        new = Node(value)
        if tmp is None:
            self.__head = new
            return
        if value < tmp.data:
            new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None and value > tmp.next_node.data:
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

