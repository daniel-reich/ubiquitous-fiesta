
def cap_space(txt):
  return ''.join([i if i.islower() else ' ' + i.lower() for i in txt])

