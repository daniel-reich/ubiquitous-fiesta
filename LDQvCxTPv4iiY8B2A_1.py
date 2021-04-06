
def same_upsidedown(txt):
  d = {'0': '0', '6': '9', '9': '6'}
  return all(a in d and d[a] == b for a, b in zip(txt, txt[::-1]))

