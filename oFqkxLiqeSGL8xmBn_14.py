
def add_two_numbers(l1, l2):
  lst1, lst2 = l1.get_data(), l2.get_data()
  lst1, lst2 = (lst1, lst2 + [0] * (len(lst1) - len(lst2))) if len(lst1) >= len(lst2) \
    else (lst1 + [0] * (len(lst2) - len(lst1)), lst2)
  paired = list(zip(lst1, lst2))
  carry = 0
  result = []
  for (a, b) in paired:
    result.append((a + b + carry) % 10)
    carry = int((a + b + carry) / 10)
  if carry != 0:
    result.append(carry)
  lst_node = ListNode(result[0])
  lst_node.add_data(result[1:])
  return lst_node

