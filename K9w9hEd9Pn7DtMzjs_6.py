
def high_low(txt):
  return str(max([int(n) for n in txt.split(' ')])) + ' ' + str(min([int(n) for n in txt.split(' ')]))

