
def even_last(lst):
  if lst == []:
    return 0
  else:
    return sum(lst[0::2]) * lst[-1]

