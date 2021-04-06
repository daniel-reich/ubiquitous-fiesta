
def priority_sort(lst, s):
  lst.sort()
  return sorted(lst, key=lambda x: x not in s)

