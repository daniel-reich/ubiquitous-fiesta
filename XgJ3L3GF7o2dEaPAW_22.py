
def shared_letters(a, b):
  a = set(a.lower())
  return ''.join(sorted(list(set([c for c in b.lower() if c in a]))))

