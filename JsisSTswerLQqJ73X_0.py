
def priority_sort(lst, s):
  return sorted(lst, key=lambda x: (not x in s, x))

