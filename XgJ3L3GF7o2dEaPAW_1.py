
def shared_letters(a, b):
  return ''.join(sorted(set(l for l in a.lower() if l in b.lower())))

