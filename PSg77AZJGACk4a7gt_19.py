
def meme_sum(a, b):
  c = str(min(a, b))
  d = str(a)[::-1]
  e = str(b)[::-1]
  f = [str(int(d[i])+ int(e[i]))[::-1] for i in range(len(c))]
  g = d[len(e):] if c==e[::-1] else e[len(d):]
  return int(g + "".join(f)[::-1])

