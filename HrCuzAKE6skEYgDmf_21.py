
def pairs(lst):
  ls=[]
  while lst:
    ls.append([lst[0],lst[-1]])
    lst=lst[1:-1]
  return ls

