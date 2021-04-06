
def adjacent_product(lst):
  mx = min(lst) * max(lst)
  l = lst[1:]
  for i in range(len(l)):
    if lst[i] * l[i] > mx:
      mx = lst[i] * l[i]
  return mx

