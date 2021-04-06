
def adjacent_product(lst):
  count = -1000000
  for x in range(1,len(lst)):
    if lst[x] * lst[x-1] > count:
      count = lst[x]*lst[x-1]
  return count

