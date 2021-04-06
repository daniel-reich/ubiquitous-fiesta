
def priority_sort(lst, s):
  b = sorted(x for x in lst if x not in s)
  a = sorted((x for x in lst if x in s), key=lambda x: list(s).index(x))
  return a + b

