
def priority_sort(lst, s):
  return sorted([i for i in lst if i in s])+sorted([i for i in lst if i not in s])

