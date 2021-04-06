
def shift_letters(txt, n):
  A=[i for i in txt if i!=' ']
  K=[i for i,v in enumerate(txt) if v==' ']
  def slipe(A,t):
    count=1
    while count<=t:
      B=list(A[-1])
      for i in A[:-1]:
        B.append(i)
      count+=1
      A=B
    return A
  C=slipe(A,n)
  for i in K:
    C.insert(i,' ')
  return ''.join(C)

