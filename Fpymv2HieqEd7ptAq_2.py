
def split(txt):
  if len(txt) == 0:
    return []
  idx, pDepth = 1, 1
  while pDepth > 0:
    pDepth += 1 if txt[idx] == "(" else -1
    idx += 1
  return [txt[:idx]] + split(txt[idx:])

