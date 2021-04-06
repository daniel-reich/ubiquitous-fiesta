
def true_alphabetic(txt):
  lengths = [len(i) for i in txt.split()]
  txt = ''.join(sorted(''.join(txt.split())))
  ret = []
  for i in lengths:
    ret.append(txt[:i])
    txt = txt[i:]
  return ' '.join(ret)

