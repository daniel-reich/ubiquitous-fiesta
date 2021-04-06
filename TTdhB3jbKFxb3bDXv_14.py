
def left_shift(lst, n):
  for i in range(0,n):
    t=lst[0]
    for j in range(0,len(lst)-1):
      lst[j]=lst[j+1]
    lst[-1]=t 
  return lst
def right_shift(lst, n):
  for i in range(0,n):
    t=lst[-1]
    for j in range(-1,-len(lst),-1):
      lst[j]=lst[j-1]
    lst[0]=t
  return lst

