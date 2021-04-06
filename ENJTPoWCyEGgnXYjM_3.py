
def percent_filled(box):
  o = ''.join(box).count('o')
  b = ''.join(box).count(' ')
  return '{}%'.format(round((o/(o+b))*100))

