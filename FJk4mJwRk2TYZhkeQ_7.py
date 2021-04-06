
def accum(txt):
  count = 1
  words = []
  for c in txt:
    s = c.lower() * (count-1)
    s = c.upper() + s
    words.append(s)
    count += 1
  return '-'.join(words)

