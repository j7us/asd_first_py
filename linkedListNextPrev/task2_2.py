from linkedListNextPrev.task2 import LinkedList2, Node


# Задание 2
# задача 2.10
# Переворот списка
# время O(n) память O(n)
def reverse(link_list: LinkedList2):
    nodes_list = []

    node = link_list.head

    while node is not None:
        nodes_list.append(node)
        link_list.delete(node.value)
        node = link_list.head

    for x in range(0, len(nodes_list)):
        link_list.add_in_head(nodes_list[x])

# Задание 2
# задача 2.11
# Проверка на циклы
# время O(n) память O(1)
def is_any_loop_in_list(link_list: LinkedList2):
    node = link_list.head

    for x in range(0, link_list.len() + 1):
        if node is None:
            return False
        node = node.next

    return True

# Задание 2
# задача 2.12
# Сортировка списка
# время O(n log n) память O(n)
def sort_list(link_list: LinkedList2) -> LinkedList2:
    if link_list.len() <= 1:
        return link_list

    list_nodes = []

    node = link_list.head
    while node is not None:
        list_nodes.append(node)
        node.prev = None
        cur_next = node.next
        node.next = None
        node = cur_next

    sorted_list = sort(list_nodes)

    link_list.clean()

    for n in sorted_list:
        link_list.add_in_tail(n)

    return link_list


def sort(list_nodes: list[Node]) -> list[Node]:
    if len(list_nodes) <= 1:
        return list_nodes

    pivot = list_nodes[0]

    eq_list = []
    max_list = []
    min_list = []

    for node in list_nodes:
        if node.value > pivot.value:
            max_list.append(node)
        elif node.value < pivot.value:
            min_list.append(node)
        else:
            eq_list.append(node)

    return sort(min_list) + eq_list + sort(max_list)


# Задание 2
# задача 2.13
# Объединение двух списков
# время O(n log n) память O(n)
def combine(list1: LinkedList2, list2: LinkedList2):
    sort_list(list1)
    sort_list(list2)

    result_list = LinkedList2()

    first_node = list1.head
    second_node = list2.head

    while first_node is not None and second_node is not None:
        if first_node.value > second_node.value:
            result_list.add_in_tail(Node(second_node.value))
            second_node = second_node.next
            continue

        result_list.add_in_tail(Node(first_node.value))
        first_node = first_node.next

    if first_node is not None:
        add_in_list(result_list, first_node)

    if second_node is not None:
        add_in_list(result_list, second_node)

    return result_list


def add_in_list(link: LinkedList2, node):
    cur = node

    while cur is not None:
        link.add_in_tail(Node(cur.value))
        cur = cur.next