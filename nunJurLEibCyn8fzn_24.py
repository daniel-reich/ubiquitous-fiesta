
def filter_list(lst):
  new=[]
  for x in lst:
    if type(x)==str:
      continue
    else:
      new.append(x)
  return new

