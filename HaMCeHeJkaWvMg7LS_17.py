
def sun_loungers(beach):
  A=[x for x in beach]
  c=0
  if len(beach)==1 and beach=='0':
    c+=1
  else:
    if (A[0], A[1])==('0', '0'):
      A[0]='1'
      c+=1
    for i in range(1, len(A)-1):
      if (A[i-1], A[i], A[i+1])==('0', '0', '0'):
        A[i]='1'
        c+=1
    if (A[-2], A[-1])==('0', '0'):
      A[-1]='1'
      c+=1
  return c

