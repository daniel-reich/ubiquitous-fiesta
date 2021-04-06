
def even_last(lst):
  if len(lst) == 0:
    return 0
  else:
    return sum([el * lst[len(lst) - 1] for idx,el in enumerate(lst) if idx % 2 == 0])

