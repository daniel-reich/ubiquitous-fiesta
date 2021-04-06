
def can_alternate(s):
  return True if abs(s.count('1') - s.count('0')) in [0,1] else False

