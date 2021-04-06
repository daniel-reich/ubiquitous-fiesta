
def pad(txt):
  return '{}{}{}'.format(txt, ' '*(1 - len(txt)%2), 'lo'*71)[:140]

