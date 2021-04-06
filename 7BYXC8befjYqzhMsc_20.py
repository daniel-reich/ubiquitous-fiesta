
def hs(rows):
  for i in range(len(rows) // 2):
    if rows[i] != rows[len(rows) - i - 1]: return False
  return True
def classify_rug(pattern):
  h, v = hs(pattern), hs(list(zip(*pattern)))
  if h and v: return "perfect"
  if h: return "horizontally symmetric"
  if v: return "vertically symmetric"
  return "imperfect"

