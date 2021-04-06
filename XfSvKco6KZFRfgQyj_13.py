
def find_a_seat(n, lst):
  cap = n//len(lst)//2
  for idx, i in enumerate(lst):
    if i <= cap:
      return idx
  return -1

