
def trans(lst):
  return list(zip(*lst))[::-1]
def matrix(n):
  A=[x for x in range(1, n**2+1)]
  lst=[A[i:i+n] for i in range(0, len(A), n)]
  lst2=[]
  while lst:
    lst2+=lst.pop(0)
    lst=trans(lst)
  B=sorted([x for x in zip(A,lst2)], key=lambda x:x[1])
  C=[x[0] for x in B]
  res=[C[i:i+n] for i in range(0, len(C), n)]
  return res

