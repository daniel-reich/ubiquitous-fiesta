
def find_odd(lst):
  for i in lst:
    if lst.count(i)%2!=0:
      return i

