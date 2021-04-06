
def mini_peaks(lst):
  a=len(lst)
  newLst=[]
  for i in range(1,a-1):
    b=lst[i]
    if(b>lst[i-1] and b>lst[i+1]):
      newLst.append(lst[i])
  return newLst

