
def odd_sort(lst):
  a = sorted([i for i in lst if i%2])
  c = a[::-1]
  b = []
  for i in lst:
    if i in a:
      b.append(c.pop())
    else:
      b.append(i)
  return b

