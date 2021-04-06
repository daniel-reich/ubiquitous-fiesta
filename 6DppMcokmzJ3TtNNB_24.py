
def true_alphabetic(txt):
  A=sorted([x for x in txt if x.isalpha()])
  B=txt.split()
  C=['']*len(B)
  k=0
  for i in range(len(B)):
    C[i]=''.join(A[k:k+len(B[i])])
    k+=len(B[i])
  return ' '.join(C)

