
def canConcatenate(lst, target):
  l=[]
  for i in lst:
    l+=i
  l.sort()
  target.sort()
  return l==target

