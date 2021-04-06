
def get_diagonals(lst):
  return [[lst[x][x] for x in range(len(lst))]] + [[lst[x][-x-1] for x in range(len(lst))] ]

