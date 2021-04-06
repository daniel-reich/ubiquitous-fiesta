
true, false = True, False
def get_diagonals(lst):
  return [[lst[i][i] for i in range(len(lst))],
      [lst[i][-i-1] for i in range(len(lst))]
       ]

