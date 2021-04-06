
def ascii_sort(lst):
  return lst[int(sum([ord(i) for i in lst[0]]) > sum([ord(i) for i in lst[1]]))]

