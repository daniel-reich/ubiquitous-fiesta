
def add_two_numbers(l1, l2):
  val1 = int("".join(str(i) for i in l1.get_data()[::-1]))
  val2 = int("".join(str(i) for i in l2.get_data()[::-1]))
  res = [int(c) for c in str(val1 + val2)[::-1]]
  node = ListNode(res[0])
  node.add_data(res[1:])
  return node

