
def int_to_vlq(n):
  s=bin(n)[2:][::-1]
  A=[s[i:i+7][::-1].zfill(7) for i in range(0,len(s),7)][::-1]
  for i in range(len(A)-1):
    A[i]='1'+A[i]
  return [int(x,2) for x in A]
  
def vlq_to_int(lst):
  C=[bin(x)[2:] for x in lst]
  for i in range(len(C)-1):
    C[i]=C[i][1:]
  for i in range(len(C)):
    C[i]=C[i].zfill(7)
  return int(''.join(C), 2)

