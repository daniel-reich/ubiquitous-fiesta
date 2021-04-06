
def maskify(txt):
  return '{}{}'.format('#' * (len(txt) - 4), txt[-4:])

