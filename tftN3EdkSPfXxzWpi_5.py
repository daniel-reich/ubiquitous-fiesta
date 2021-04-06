
def sentence_searcher(txt, n):
  s=txt[:-1]
  t=s.split('. ')
  A=[0]+[len(x.split()) for x in t]
  B=[sum(A[:i]) for i in range(1,len(A)+1)]
  n=(n+sum(A))%sum(A)
  for i in range(len(B)-1):
    if B[i]<=n<B[i+1]:
      return t[i]+'.'

