
from functools import reduce
​
def add_two_numbers(l1, l2):
    addition = list_node_to_int(l1) + list_node_to_int(l2)
    lst = list(map(int, str(addition)))
    ln = ListNode(lst.pop())
    ln.add_data(lst[::-1])
    return ln
​
def list_node_to_int(ln):
    return reduce(lambda i, d: i*10 +d, ln.get_data()[::-1], 0)

