
def mystery_func(s):
  return ''.join(c * int(i) for c, i in zip(*[iter(s)] * 2))

