
def find_a_seat(n, lst):
  m=n/len(lst)
  for i,x in enumerate(lst):
    if x/m<=.5:
      return i
  return -1

