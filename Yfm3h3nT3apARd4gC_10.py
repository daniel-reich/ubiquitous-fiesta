
def rolls(lst):
  array = lst
  for x in range(len(array)):
    if x != 0:
      if array[0 - (x + 1)] == 1:
        array[0 - x] = 0
      elif array[0 - (x + 1)] == 6:
        array[0 - x] *= 2
  return sum(array)

