
def upward_trend(lst):
  for i,x in enumerate(lst):
    if type(x)!=int:
      return "Strings not permitted!"
  return lst==sorted(lst)

