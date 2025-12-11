class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
        self.count += 1

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result_nodes = []
        node = self.head

        while node is not None:
            if node.value == val:
                result_nodes.append(node)
            node = node.next

        return result_nodes

    def delete(self, val, all=False):
        node = self.head
        continue_delete = True

        while node is not None and continue_delete:
            if node.value == val:
                self.__remove_node(node)
                continue_delete = all
            node = node.next

    def __remove_node(self, node):
        self.count -= 1
        current_prev = node.prev
        current_next = node.next

        if self.head == node:
            self.head = current_next

        if self.tail == node:
            self.tail = current_prev

        if current_prev is not None:
            current_prev.next = current_next

        if current_next is not None:
            current_next.prev = current_prev

    def clean(self):
        self.head = None
        self.tail = None
        self.count = 0

    def len(self):
        return self.count # здесь будет ваш код

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
            return

        self.count += 1
        current_next = afterNode.next

        afterNode.next = newNode
        newNode.prev = afterNode
        newNode.next = current_next

        if current_next is not None:
            current_next.prev = newNode
            return

        self.tail = newNode

    def add_in_head(self, newNode):
        self.count += 1
        current_head = self.head

        self.head = newNode
        newNode.next = current_head

        if current_head is not None:
            current_head.prev = newNode
            return

        self.tail = newNode

