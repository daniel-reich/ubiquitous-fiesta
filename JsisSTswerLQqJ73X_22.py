
def priority_sort(lst, s):
  return sorted(sorted(lst), key=lambda x: x not in s)

