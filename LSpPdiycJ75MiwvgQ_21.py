
def grid_pos(lst):
  f = lst[0] + lst[1]
  fact = 1
  for i in range(1,lst[1]+1):
    fact *= i
  i = f
  fact2 = 1
  while True:
    if i > lst[0]:
      fact2 *= i
    else:
      break
    i -= 1
  return round(fact2 / fact)

