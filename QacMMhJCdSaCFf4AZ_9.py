
def sequence_generator(seq):
  a=seq[1]-seq[0]
  c=seq[0]-a
  out=[ a*(n+1) +c for n,x in enumerate(seq)]
  print(a,c,seq,out)
  if out==seq:
    return lambda n: a*n + c
  
  a=seq[1]//seq[0]
  c=seq[0]//a
  return lambda n: a**n * c

