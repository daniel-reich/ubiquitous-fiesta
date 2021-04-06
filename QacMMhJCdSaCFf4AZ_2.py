
def sequence_generator(seq):
  if seq[0] - 2*seq[1] +seq[2] == 0:
    return lambda n: (seq[1]-seq[0])*n + 2*seq[0] - seq[1]
  else:
    return lambda n: (seq[1]/seq[0])**n*(seq[0]**2/seq[1])

