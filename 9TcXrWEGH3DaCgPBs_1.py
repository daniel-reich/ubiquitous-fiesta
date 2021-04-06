
def find_odd(lst):
  return [x for x in set(lst) if lst.count(x)%2!=0][0]

