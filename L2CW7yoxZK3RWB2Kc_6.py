
def nico_cipher(m, k):
  m = m + ' '*(len(k)-(len(m) % len(k))) if len(m) % len(k) else m
  s, t = str(), {c: i for i, c in enumerate(sorted(k))}
  v = {i: t[x] for i, x in enumerate(k)}
  for i in range(len(m)//len(k)):
    w = [[c, v[n]] for n, c in enumerate(m[i*len(k):(i+1)*len(k)])]
    s += ''.join(a for a, b in sorted(w, key=lambda x: x[1]))
  return s

