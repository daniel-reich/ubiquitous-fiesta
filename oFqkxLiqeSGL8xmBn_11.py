
def add_two_numbers(l1, l2):
  n1 = int(''.join(str(d) for d in l1.get_data()[::-1]))
  n2 = int(''.join(str(d) for d in l2.get_data()[::-1]))
  n = str(n1 + n2)[::-1]
  ans = ListNode(int(n[0]))
  ans.add_data(list(map(int, list(n[1:]))))
  return ans

