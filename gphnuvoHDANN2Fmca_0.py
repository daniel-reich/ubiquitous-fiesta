
def odd_sort(lst): 
  odds = iter(sorted(i for i in lst if i%2))
  return [next(odds) if n%2 else n for n in lst]

