
def sort_by_string(lst, txt):
  new = []
  for i in txt:
    for j in lst:
      if i == j[0]:
        new.append(j)
  return new

