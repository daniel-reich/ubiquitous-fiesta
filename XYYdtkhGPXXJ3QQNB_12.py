
def num_in_str(lst):
  finalLst = []
  for i in lst:
    add = False
    for e in i:
      if e.isdigit():
        add = True
    if add:
      finalLst.append(i)
  
  return finalLst

