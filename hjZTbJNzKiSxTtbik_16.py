
def sort_by_string(lst, txt):
  newlst =[]
  for t in txt:
    for l in lst:
      if l[0] == t:
        newlst.append(l)
  return newlst

