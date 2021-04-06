
def add_two_numbers(l1, l2):
  l1, l2 = l1.get_data()[::-1], l2.get_data()[::-1]
  l1, l2 = ''.join(map(str, l1)), ''.join(map(str, l2))
  lst = list(map(int, str(int(l1) + int(l2))[::-1]))
  out = ListNode(lst.pop(0))
  out.add_data(lst)
  return out

