
def removeDups(lst):
  s=[]
  for x in lst:
    if x not in s:
      s.append(x)
  return s

