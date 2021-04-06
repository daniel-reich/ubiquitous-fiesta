
def mystery_func(txt):
  return ''.join([x*int(y) for (x,y) in zip(txt[::2],txt[1::2])])

