
def possible_path(lst):
  odd = lst[::2]
  even = lst[1::2]
  if type(lst[0]) == int:
    return all(type(i) == str for i in even) and all(type(i) == int for i in odd)
  elif type(lst[0]) == str:
    return all(type(i) == str for i in odd) and all(type(i) == int for i in even)

