
def complete_square(lst):
  if len(lst) < len(lst[0]):
    lst.extend([[0] * len(lst[0])] * (len(lst[0]) - len(lst)))
  elif len(lst) > len(lst[0]):
    for row in lst:
      row.extend([0] * (len(lst) - len(row)))
  return lst

