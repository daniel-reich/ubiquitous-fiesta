
def single_number(lst):
  for i in set(lst):
    if lst.count(i) == 1:
      return i

