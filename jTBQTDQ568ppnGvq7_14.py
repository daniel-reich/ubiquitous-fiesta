
def digit_sort(lst):
  d = {}
  for num in lst:
    l = len(str(num))
    d[l] = d.get(l,[]) + [num]
  slens = list(d.keys())
  slens.sort(reverse = True)
  new = []
  for n in slens:
    d[n].sort()
    new.extend(d[n])
  return new

