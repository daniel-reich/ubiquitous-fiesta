
def mystery_func(txt):
  return ''.join([int(y)*x for x,y in zip(txt[0::2], txt[1::2])])

