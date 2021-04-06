
def priority_sort(lst, s):
  l = sorted(list(s))
  return [x for x in sorted(lst) if x in l] + sorted(x for x in lst if x not in l)

