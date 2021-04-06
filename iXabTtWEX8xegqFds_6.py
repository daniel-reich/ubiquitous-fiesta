
def alternate_sort(lst):
  n = sorted(filter(lambda v: isinstance(v, str), lst)) 
  a = sorted(filter(lambda v: isinstance(v, int), lst))
  return [val for pair in list(zip(a, n)) for val in pair]

