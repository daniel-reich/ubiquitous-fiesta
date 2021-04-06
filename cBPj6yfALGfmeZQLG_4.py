
def vertical_txt(txt):
  words = txt.split()
  return [list(i) for i in zip(*['{:{}}'.format(w, max(len(i) for i in words)) for w in words])]

