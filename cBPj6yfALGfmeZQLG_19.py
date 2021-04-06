
def vertical_txt(txt):
  txt = txt.split()
  maxl= max(len(w) for w in txt)
  txt = [w+' '*(maxl-len(w)) for w in txt]
  return [list(x) for x in zip(*txt)]

