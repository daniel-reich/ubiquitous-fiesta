
def find_a_seat(n, lst):
  max_capacity = n/len(lst)
  for i in range(len(lst)):
    if lst[i]<=max_capacity/2:
      return i
  return -1

