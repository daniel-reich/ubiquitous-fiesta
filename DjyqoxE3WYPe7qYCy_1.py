
def reverse_odd(txt):
  return ' '.join(w[::-1] if len(w) % 2 else w for w in txt.split())

