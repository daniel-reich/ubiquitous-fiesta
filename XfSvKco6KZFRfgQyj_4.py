
def find_a_seat(n, lst):
  capacity = n / len(lst)
  
  for idx, i in enumerate(lst):
    if i <= capacity / 2:
      return idx
  return -1

