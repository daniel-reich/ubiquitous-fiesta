
def priority_sort(lst, s):
  return sorted(lst, key=lambda i: (1-(i in s), i))

