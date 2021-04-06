
def split(txt):
  return ''.join([x for x in txt if x in 'aeiou']+[x for x in txt if x not in 'aeiou'])

