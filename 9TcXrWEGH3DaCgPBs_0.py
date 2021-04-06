
def find_odd(lst):
  for num in lst:
    if lst.count(num) % 2:
      return num

