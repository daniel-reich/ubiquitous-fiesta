
def sequence_generator(seq):
  A=[y-x for x, y in zip(seq, seq[1:])]
  G=[y/x for x, y in zip(seq, seq[1:])]
  if len(set(A))==1:
    return lambda n: seq[0]+(seq[1]-seq[0])*(n-1)
  else:
    return lambda n: int(seq[0]*(seq[1]/seq[0])**(n-1))

