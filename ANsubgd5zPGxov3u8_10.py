
def initialize(names):
  ret = []
  for i in names:
    s = i.split()
    ret.append('{}. {}.'.format(s[0][0], s[1][0]))
  
  return ret

