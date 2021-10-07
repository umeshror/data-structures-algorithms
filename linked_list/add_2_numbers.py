class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "{}, Node({})".format(str(self.val), str(self.next))


def generate_nodes(arr):
    """
    :param arr: List of values
    :return: Head of Linked List
    """
    if not arr:
        return arr
    node = Node(arr[0])
    head = node
    for item in arr[1:]:
        node.next = Node(item)
        node = node.next
    return head


list_1 = generate_nodes([2, 4, 3])
list_2 = generate_nodes([5, 6, 4])


def merge_two_lists(l1, l2, carry=0, node=Node(0)):
    """
    :type l1: Head Node 1 : 2, 4, 3
    :type l2: Head Node 2 : 5, 6, 4
    """

    summ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

    node.val = summ % 10
    if l1.next and l2.next:
        node.next = Node(0)
        merge_two_lists(l1.next, l2.next, summ // 10, node.next)
    return node


merge_two_lists(list_1, list_2)
merge_two_lists(generate_nodes([0]), generate_nodes([0]))
merge_two_lists(generate_nodes([0, 1]), generate_nodes([2]))

