
def spartans_cipher(m, n, s=None):
  if s is None:
    if len(m) % n: m += ' '*((len(m)//n+1)*n-len(m))
    s, n = [], len(m)//n
  if not len(m): return ''.join(''.join(k) for k in zip(*s)).strip()
  return spartans_cipher(m[n:], n, s + [list(m[:n])])

