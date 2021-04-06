
def bifid(s):
  z = 'abcdefghiklmnopqrstuvwxyz'
  n = [str((i // 5 + 1) *10 + i % 5 + 1) for i in range(26)]
  d = dict(zip(z, n))
  r = {v : k for k, v in d.items()}
  
  if ' ' in s:
    s = ''.join(c for c in s.lower() if c.isalpha()).replace("j", "i")
    p = ''.join(d[c] for c in s)
    cip = p[::2] + p[1::2]
    return ''.join(r[cip[n:n+2]] for n in range(0, len(cip), 2))
    
  else:
    p = ''.join(d[c] for c in s)
    b, e = p[:len(p)//2], p[len(p)//2:]
    cip = list(zip(b, e))
    return ''.join(r[''.join(x)] for x in cip)

