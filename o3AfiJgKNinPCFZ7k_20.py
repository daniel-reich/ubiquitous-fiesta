
def partition(txt, n):
  ret = []
  while len(txt)>0:
    ret.append(txt[:n])
    txt = txt[n:]
  if txt:
    ret.append(txt)
  return ret

