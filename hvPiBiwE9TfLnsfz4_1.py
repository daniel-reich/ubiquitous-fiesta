
def generate_word(n, w=None):
  if w is None: w = ['b', 'a']
  return 'invalid' if n < 2 else ', '.join(w) \
    if len(w) == n else generate_word(n, w+[w[-2]+w[-1]])

