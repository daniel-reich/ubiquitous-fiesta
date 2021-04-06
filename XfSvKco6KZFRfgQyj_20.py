
def find_a_seat(n, lst):
  capacity = n / len(lst)
  for c in lst:
    if c / capacity <= 0.5:
      return lst.index(c)
  return -1

