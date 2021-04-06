
def shift_sentence(txt):
  t = txt.split()
  if len(t)==1: return txt
  f = [x[0] for x in t]
  f.insert(0,f.pop(-1))
  return ' '.join(f[i] + t[i][1:] for i in range(len(t)))

