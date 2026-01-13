class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.count = 0
        self.__ascending = asc
        self.asc_insert_before = {True: lambda x: x >= 0, False: lambda x: x <= 0}

    def compare(self, v1, v2):
        res = v1 - v2
        return -1 if res < 0 else 1 if res > 0 else 0

    def add(self, value):
        self.count += 1
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        asc = self.__ascending
        node_to_insert = Node(value)
        node = self.head
        inserted = False

        while node is not None:
            comp_res = self.compare(node.value, value)

            if self.asc_insert_before[asc](comp_res):
                self.__insert_before(node, node_to_insert)
                inserted = True
                break

            node = node.next

        if not inserted:
            self.__insert_after(self.tail, node_to_insert)


    def __insert_before(self, before: Node, node: Node):
        cur_prev = before.prev
        node.prev = cur_prev
        node.next = before
        before.prev = node

        if before == self.head:
            self.head = node
        else:
            cur_prev.next = node


    def __insert_after(self, after: Node, node: Node):
        cur_next = after.next
        node.next = cur_next
        after.next = node
        node.prev = after

        if after == self.tail:
            self.tail = node


    def find(self, val):
        if self.count == 0:
            return None

        node = self.head
        asc = self.__ascending

        while node is not None:
            if node.value == val:
                return node

            comp_res = self.compare(node.value, val)

            if self.asc_insert_before[asc](comp_res):
                return None
            node = node.next

        return None

    def delete(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                self.__remove_node(node)
                self.count -= 1
                return
            node = node.next

    def __remove_node(self, node):
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

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        self.count = 0

    def len(self):
        return self.count # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1_s = v1.strip()
        v2_s = v2.strip()
        return -1 if v1_s < v2_s else 1 if v1_s > v2_s else 0

