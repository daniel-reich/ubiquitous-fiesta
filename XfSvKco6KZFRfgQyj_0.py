
def find_a_seat(n, lst):
  a = n//len(lst)
  return [[i for i, j in enumerate(lst) if j/a<=0.5]+[-1]][0][0]

