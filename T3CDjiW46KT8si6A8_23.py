
def product(lst):
  lst.sort(reverse=True)
  for n in lst[1:]:
    if n != lst[0]:
      return n * lst[0]
  return lst[0]**2

