
def find_a_seat(n, lst):
  c = n/len(lst)
  h = c/2
  for i in range(len(lst)):
    if lst[i] <= h:
      return i
  return -1

