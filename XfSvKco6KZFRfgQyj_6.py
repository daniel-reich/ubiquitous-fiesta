
def find_a_seat(n, lst):
  m=n//len(lst)
  for i in range(len(lst)):
    if lst[i]/m<=0.5:
      return i
  return -1

