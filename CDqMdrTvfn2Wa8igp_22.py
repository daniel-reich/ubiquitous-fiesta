
def next_element(lst):
  if lst[0] == lst[1]:
    return lst[0]
  elif lst[0] > lst[1]:
    x = lst[0] - lst[1]
    return (lst[-1]-x)
  else:
    x = lst[1] - lst[0]
    return (lst[-1]+x)

