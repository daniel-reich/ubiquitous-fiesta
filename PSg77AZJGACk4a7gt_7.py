
def meme_sum(a, b):
  txt = ""
  a, b = (str(x) for x in sorted([a, b]))
  for i in range(1, len(b) + 1):
    txt = (str(int(a[-i]) + int(b[-i])) if len(a) >= i else b[-i]) + txt
  return int(txt)

