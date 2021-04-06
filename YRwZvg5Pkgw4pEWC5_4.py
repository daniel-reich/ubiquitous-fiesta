
def flick_switch(lst):
  if lst:
    A=[]
    for x in lst:
      if x!='flick':
        A.append(True)
      else:
        A.append(False)
    B=[]
    B.append(A[0])
    for i in range(1, len(A)):
      B.append(B[-1]==A[i])
    return B
  return []

