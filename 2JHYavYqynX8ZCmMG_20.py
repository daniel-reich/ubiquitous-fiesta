
def ascii_sort(lst):
  return lst[1] if sum(map(lambda x: ord(x), lst[0])) >= sum(map(lambda x: ord(x), lst[1]))else lst[0]

