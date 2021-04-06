
def rearranged_difference(num):
  A=[int(x) for x in str(num)]
  B=sorted(A)
  C=[str(x) for x in B if x]
  D=[str(x) for x in B[::-1]]
  a=int(''.join(C))
  b=int(''.join(D))
  return b-a

