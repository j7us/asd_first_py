class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        self.length += 1

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head

        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next

        return result

    def delete(self, val, all=False):
        node = self.head
        prev = None
        delete_continue = True

        while node is not None and delete_continue:
            if node.value == val:
                self.__remove_node(node, prev)
                self.length -= 1
                delete_continue = all

            prev = node if prev is not None and prev.next == node else prev
            node = node.next

    def __remove_node(self, node, prev):
        node_next = node.next

        if self.tail == node:
            self.tail = node_next

        if prev is None:
            self.head = node_next
        else:
            prev.next = node_next

    def clean(self):
        self.head = None
        self.tail = None
        self.length = 0

    def len(self):
        return self.length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.__add_in_head(newNode)
            self.length += 1
            return

        current_next = afterNode.next
        newNode.next = current_next
        afterNode.next = newNode

        if self.tail == afterNode:
            self.tail = newNode
        self.length += 1


    def __add_in_head(self, node):
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

