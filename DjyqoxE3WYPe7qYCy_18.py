
def reverse_odd(txt):
  rev = lambda w : w if len(w)%2 == 0 else w[::-1]
  return ' '.join(map(rev,txt.split()))

