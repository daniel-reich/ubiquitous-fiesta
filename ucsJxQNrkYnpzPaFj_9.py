
def char_appears(s,c):
  return [x.count(c.lower()) for x in s.lower().split()]

