
is_arithmetic = lambda s : len(set(j-i for i,j in zip(s, s[1:]))) == 1
​
def sequence_generator(seq):
  if is_arithmetic(seq):
    return lambda n : seq[0] + (seq[1] - seq[0]) * (n - 1)
  else:
    return lambda n : seq[0] * (seq[1] / seq[0]) ** (n - 1)

