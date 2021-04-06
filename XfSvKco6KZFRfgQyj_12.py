
def find_a_seat(n, lst):
  a=(n/len(lst))/2
  for i in range(len(lst)):
    if lst[i]<=a:return i
  return -1

