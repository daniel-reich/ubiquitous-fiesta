
def landscape_type(lst):
  A=[]
  for i in range(len(lst)-1):
    if lst[i]<lst[i+1]:
      A.append(1)
    elif lst[i]>lst[i+1]:
      A.append(-1)
    else:
      A.append(0)
  B=[x for x in A if x]
  c=0
  for i in range(len(B)-1):
    if B[i]*B[i+1]<0:
      c+=1
    else:
      c+=0
  if c!=1:
    return "neither"
  else:
    if B[0]==1:
      return "mountain"
    else:
      return "valley"

