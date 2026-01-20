from ordered.task7 import OrderedList

# Задание 7
# задача 8
# Удаление дубликатов
# время O(n)
class NodeForDuplicateTask:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedListWithDuplicateRemove:
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
            self.head = NodeForDuplicateTask(value)
            self.tail = self.head
            return

        asc = self.__ascending
        node_to_insert = NodeForDuplicateTask(value)
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


    def __insert_before(self, before, node):
        cur_prev = before.prev
        node.prev = cur_prev
        node.next = before
        before.prev = node

        if before == self.head:
            self.head = node
        else:
            cur_prev.next = node


    def __insert_after(self, after, node):
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

        self.count -= 1

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

    def remove_duplicates(self):
        node = self.head.next
        val = self.head.value if self.head is not None else None

        while node is not None:
            if node.value == val:
                self.__remove_node(node)

            val = node.value
            node = node.next


# Задание 7
# задача 9
# Слияние двух упорядоченных списков
# время O(n)
def merge_lists(l1, l2):
    asc_next_node = {
        True: lambda x: x.next if x is not None else None,
        False: lambda x: x.prev if x is not None else None,
    }
    asc_start_node = {
        True: lambda x: x.head,
        False: lambda x: x.tail
    }
    comparing_values_action = {
        True: lambda x, y: x.value - y.value <= 0,
        False: lambda x, y: x.value - y.value >= 0
    }

    l1_asc = find_list_asc(l1)
    l2_asc = find_list_asc(l2)

    if l1_asc != l2_asc:
        raise Exception('Разный asc у списков')

    result = OrderedList(l1_asc)

    l1_node = asc_start_node[l1_asc](l1)
    l2_node = asc_start_node[l2_asc](l2)
    l1_next_node_action = asc_next_node[l1_asc]
    l2_next_node_action = asc_next_node[l2_asc]
    compare = comparing_values_action[l1_asc]

    while l1_node is not None or l2_node is not None:
        all_nodes_have_val = l1_node is not None and l2_node is not None
        l1_inserted = (all_nodes_have_val and compare(l1_node, l2_node)) or l2_node is None
        result.add(l1_node.value if l1_inserted else l2_node.value)

        if l1_inserted:
            l1_node = l1_next_node_action(l1_node)
        else:
            l2_node = l2_next_node_action(l2_node)

    return result

def find_list_asc(l1):
    node = l1.head
    val = None

    while node is not None:
        if val is not None and val != node.value:
            return node.value - val > 0
        val = node.value
        node = node.next

    return True

# Задание 7
# задача 10
# Нахождение под-списка
# время O(n)
class NodeWithSubListFunc:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedListWithSubListFunc:
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
            self.head = NodeWithSubListFunc(value)
            self.tail = self.head
            return

        asc = self.__ascending
        node_to_insert = NodeWithSubListFunc(value)
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


    def __insert_before(self, before, node):
        cur_prev = before.prev
        node.prev = cur_prev
        node.next = before
        before.prev = node

        if before == self.head:
            self.head = node
        else:
            cur_prev.next = node


    def __insert_after(self, after, node):
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

    def find_sub_list(self, sub_list):
        sub_node = sub_list.head
        node = self.head

        while node is not None and sub_node is not None:
            if node.value == sub_node.value:
                sub_node = sub_node.next
            else:
                sub_node = sub_list.head

            node = node.next

        return sub_node is None


# Задание 7
# задача 11
# Нахождение самого популярного значения в списке
# время O(n)
def find_popular_value(l):
    value_count = {}
    node = l.head
    res = None

    while node is not None:
        value_count[node.value] = value_count.get(node.value, 0) + 1
        res = node.value if res is None or value_count[node.value] > value_count[res] else res
        node = node.next

    return res

# Задание 7
# задача 12
# Нахождение индекса по значению за log n
# время O(log n)
class NodeWithIndex:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedListWithIndex:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.count = 0
        self.array = []
        self.__ascending = asc
        self.asc_insert_before = {True: lambda x: x >= 0, False: lambda x: x <= 0}

    def compare(self, v1, v2):
        return -1 if v1 < v2 else 1 if v1 > v2 else 0

    def add(self, value):
        self.count += 1
        if self.head is None:
            self.head = NodeWithIndex(value)
            self.tail = self.head
            return

        asc = self.__ascending
        node_to_insert = NodeWithIndex(value)
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

        self.array = self.get_all()




    def __insert_before(self, before, node):
        cur_prev = before.prev
        node.prev = cur_prev
        node.next = before
        before.prev = node

        if before == self.head:
            self.head = node
        else:
            cur_prev.next = node


    def __insert_after(self, after, node):
        cur_next = after.next
        node.next = cur_next
        after.next = node
        node.prev = after

        if after == self.tail:
            self.tail = node


    def find(self, val):
        if self.count == 0:
            return None

        ind = self.find_index(val)

        return self.array[ind] if ind >= 0 else None

    def delete(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                self.__remove_node(node)
                self.count -= 1
                self.array = self.get_all()
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
        self.array = []

    def len(self):
        return self.count # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def find_index(self, val):
        min_index = 0
        max_index = len(self.array) - 1
        asc = self.__ascending
        next_indexes_by_asc = {
            True: lambda mi, ma, mid, comp: (mid + 1, ma) if comp < 0 else (mi, mid + 1),
            False: lambda mi, ma, mid, comp: (mi, mid + 1) if comp < 0 else (mid + 1, ma)
        }

        while min_index <= max_index:
            mid_index = (min_index + max_index) // 2
            node_mid = self.array[mid_index]

            comp_res = self.compare(node_mid.value, val)

            if comp_res == 0:
                return mid_index

            min_index, max_index = next_indexes_by_asc[asc](min_index, max_index, mid_index, comp_res)

        return -1


# Рефлексия задач задания 5:
# 3. Вращение очереди по кругу на N элементов.
# Задание выполнено верно

# 4. Очередь с помощью двух стеков.
# Задание выполнено верно

# 5. Обращение всех элементов в очереди в обратном порядке.
# Задание выполнено верно

# 6. Циклическая буферную очередь на базе статического массива фиксированного размера
# Задача реализована неправильно, не был добавлен head и tail, а просто использовался массив
# с count и capacity, где удаление и добавление происходило в конце массива

