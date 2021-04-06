
def insSorted(lst,n,leftIdx,rightIdx):
  print(lst,n,leftIdx,rightIdx)
  if not lst or leftIdx==len(lst) or leftIdx>rightIdx:
    lst.insert(leftIdx,n)
    return leftIdx
  midIdx=leftIdx+(rightIdx-leftIdx)//2
  if n<lst[midIdx]: return insSorted(lst,n,leftIdx,midIdx-1)
  elif n>lst[midIdx]: return insSorted(lst,n,midIdx+1,rightIdx)
  else:
    i=midIdx
    while i>=0 and lst[i]==n: i-=1
    lst.insert(i+1,n)
    return i+1
​
def left_side(lst):
  sortedLst=[]
  res=[]
  for x in lst:
    res.append(insSorted(sortedLst,x,0,len(sortedLst)))
  return res
​
def right_side(lst):
  sortedLst=[]
  res=[]
  for x in lst[::-1]:
    res.append(insSorted(sortedLst,x,0,len(sortedLst)))
  res.reverse()
  return res

