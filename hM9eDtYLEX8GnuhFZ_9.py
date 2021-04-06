
def random(lst):
  B=[]
  for i in range(65535):
    if (i*lst[0]+1)%65535==lst[1]:
      B.append(i)
  if len(B)==1:
    return (B[0]*lst[1]+1)%65535
  else:
    return None

