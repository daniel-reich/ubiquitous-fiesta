
def sort_by_string(lst, txt):
  a = []
  for x in txt: 
    for y in lst:
      if x == y[0]:
        a.append(y)
      else:
        pass
  return a

