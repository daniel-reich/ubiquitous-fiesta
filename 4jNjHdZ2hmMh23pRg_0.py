
def cutting_grass(lst, *cuts):
  o = []
  for c in cuts:
    lst = [i - c for i in lst]
    if min(lst) >= 1:
      o.append(lst)
    else:
      o.append("Done")
  return o

