
def find_odd(lst):
  for i in set(lst):
    if lst.count(i) % 2 == 1:
      return i

