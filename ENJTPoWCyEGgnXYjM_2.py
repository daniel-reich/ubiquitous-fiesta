
def percent_filled(box):
  box = ''.join(box)
  o = box.count('o')
  s = box.count(' ')
  return "{0:.0%}".format(o / (o+s))

