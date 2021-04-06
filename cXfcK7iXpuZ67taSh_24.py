
def mystery_func(txt):
  return ''.join(txt[::2][n] * int(txt[1::2][n]) for n in range(len(txt[::2])))

