
def larger_than_right(lst):
  i=0
  a=[]
  while i<len(lst)-1:
   if lst[i]>max(lst[i+1:]) : a.append(lst[i])
   i+=1
  a.append(lst[-1])
  return a

