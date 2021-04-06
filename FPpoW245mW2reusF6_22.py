
def even_last(lst):
  if lst ==[]:
    return 0
  y = 0
  for x in range(0, len(lst), 2):
    y += lst[x]
  return y * lst[-1]

