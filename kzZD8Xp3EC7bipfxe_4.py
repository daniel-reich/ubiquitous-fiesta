
def worded_math(s):
  W = 'zero one two plus minus'.split()
  for a, b in zip(W, '0 1 2 + -'.split()):
    s = s.lower().replace(a, b)
  return W[eval(s)].title()

