
def multiply_by_11(n):
  m=n[::-1]
  A=[int(x) for x in m[:-1]]
  B=[int(x) for x in m[1:]]
  C=[divmod(A[i]+B[i],10) for i in range(len(A))]
  D=[x[1] for x in C]
  E=[x[0] for x in C]
  F=[D[0]]+[D[i+1]+E[i] for i in range(len(D)-1)]
  c=E[-1]+B[-1]
  for i in range(len(F)):
    if F[i]==10:
      F[i]=0
      F[i+1]+=1
  G=[A[0]]+F+[c]
  return ''.join([str(x) for x in G[::-1]])

