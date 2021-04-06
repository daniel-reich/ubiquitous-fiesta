
def meme_sum(a, b):
  k, t=str(a), str(b)
  m=max(len(k), len(t))
  k, t=k.zfill(m), t.zfill(m)
  A=[str(int(k[i])+int(t[i])) for i in range(m)]
  return int(''.join(A))

