
def cutting_grass(lst, *cuts):
  a = []
  for i in cuts:
    lst = [j - i for j in lst]
    if sum([k <= 0 for k in lst]) > 0:
      a.append('Done')
    else:
      a.append(lst)
  return a

