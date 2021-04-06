
def ascii_sort(lst):
  first = sum([ord(i) for i in lst[0]])
  second = sum([ord(i) for i in lst[1]])
  if first < second:
    return lst[0]
  return lst[1]

