
def word_builder(l, p):
  return ''.join(c[0] for c in sorted([i for i in zip(l,p)],key=lambda x:x[1]))

