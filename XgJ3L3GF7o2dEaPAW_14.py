
def sharedLetters(a, b):
  set_a, set_b = set(a.lower()), set(b.lower())
  return ''.join(sorted(set_a.intersection(set_b)))

