
def get_diagonals(lst):
  ll = []
  lr = []
  for i in range(1, len(lst) + 1):
    ll.append(lst[i - 1][i - 1])
    lr.append(lst[i - 1][-i])
  return [ll, lr]

