
def pilish_string(txt):
  pi = map(int, '314159265358979')
  lst = []
  for d in pi:
    if not txt: break
    s = txt[:d]
    lst.append((s+s[-1]*d)[:d])
    txt = txt[d:]
  return ' '.join(lst)

