
def flip_list(lst):
  if lst == []:
    return []
  else:
    if isinstance(lst[0], list) == True:
      a = []
      for i in lst:
        for b in i:
          a.append(b)
      return a
    else:
      return [[x] for x in lst]

