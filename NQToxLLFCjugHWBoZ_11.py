
def sort_by_character(lst, n):
  a = []
  for x in lst:
    a.append(x[n-1])
  print(a)
  a.sort()
  print(a)
  b = []
  for x in a:
    for y in lst:
      if y[n-1] == x:
        b.append(y)
  print(b)
  return b

