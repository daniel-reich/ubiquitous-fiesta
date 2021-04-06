
def ascii_sort(lst):
  return lst[0] if sum([ord(x) for x in lst[0]]) < sum([ord(x) for x in lst[1]]) else lst[1]

