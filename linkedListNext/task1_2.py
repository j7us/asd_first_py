from linkedListNext.task1 import LinkedList, Node

# Задание 1
# задача 1.8
# Сумма значений узлов двух списков
# время O(n) память O(1)
#
def list_sum(list1: LinkedList, list2: LinkedList) -> LinkedList:
    if list1.len() != list2.len():
        return LinkedList()

    result_list = LinkedList()
    node_first = list1.head
    node_second = list2.head

    while node_first is not None:
        result_list.add_in_tail(Node(node_first.value + node_second.value))
        node_first = node_first.next
        node_second = node_second.next

    return result_list

