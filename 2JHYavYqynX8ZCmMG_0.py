
def ascii_sort(lst):
  return sorted(lst, key=lambda l: sum(map(ord, l)))[0]

