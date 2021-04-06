
def blah_blah(txt, n):
  A=txt.split()
  if n>len(A):
    A=['blah']*(len(A)-1)+['blah...']
  else:
    A=A[:-n]+['blah']*(n-1)+['blah...']
  return ' '.join(A)

