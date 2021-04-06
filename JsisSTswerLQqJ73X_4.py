
def priority_sort(lst, s):
  hi = [i for i in lst if i in s]
  normal = [i for i in lst if i not in s]
  return sorted(hi) + sorted(normal)

