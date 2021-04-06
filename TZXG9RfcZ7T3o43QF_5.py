
def same_length(txt):
  c = 0
  for d in txt:
    c += [-1, 1][int(d)]
    if c < 0: return False
  return not c

