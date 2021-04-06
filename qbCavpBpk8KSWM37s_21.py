
def largest_gap(lst):
  lst.sort()
  x = 0
  for n1, n2 in enumerate(lst[1:]):
    if n2-lst[n1] > x:
      x = n2-lst[n1]
  return x

