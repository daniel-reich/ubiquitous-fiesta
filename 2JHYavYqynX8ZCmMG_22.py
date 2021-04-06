
def ascii_sort(lst):
  a = sum(ord(l) for l in lst[0])
  b = sum(ord(l) for l in lst[1])
  return lst[1] if a > b else lst[0]

