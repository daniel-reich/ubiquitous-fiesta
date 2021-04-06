
def sequence_generator(seq):
  if seq[2] - seq[1] == seq[1] - seq[0]:
    func = lambda x: (seq[1] - seq[0]) * x + seq[0]
  else:
    func = lambda x: pow((seq[1]//seq[0]),x) * seq[0]
  return lambda y: func(y-1)

