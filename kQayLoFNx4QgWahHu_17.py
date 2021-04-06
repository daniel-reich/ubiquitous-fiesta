
def order(lst):
  ij_list = []
  for i, j in enumerate(lst):
    ij_list.append((j, i))
  return [el[1] for el in sorted(ij_list)]

