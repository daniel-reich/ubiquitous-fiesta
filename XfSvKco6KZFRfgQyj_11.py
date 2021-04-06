
def find_a_seat(n, lst):
  avg = n/len(lst)
  for i in range(len(lst)):
    if lst[i]<=avg/2: return i
  return -1

