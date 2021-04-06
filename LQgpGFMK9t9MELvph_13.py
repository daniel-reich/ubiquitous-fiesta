
def get_diagonals(lst):
  if lst == []:
    return [[],[]]
  l = len(lst)
  if l == 1:
    return [lst[0], lst[0]]
  ld = []
  rd = []
  for i in range(l):
    ld.append(lst[i][i])
    rd.append(lst[i][l-1-i])
  return [ld, rd]

