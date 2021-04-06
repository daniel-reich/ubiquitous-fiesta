
def word_builder(l, p):
  return ''.join(i[0] for i in sorted(zip(l, p), key=lambda x: x[-1]))

