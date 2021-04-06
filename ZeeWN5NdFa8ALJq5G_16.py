
def nearest_chapter(ch, p):
  out = sorted(ch.keys(), key = lambda x: ch[x], reverse = True)
  out.sort(key = lambda x: abs(ch[x] - p))
  return out[0]

