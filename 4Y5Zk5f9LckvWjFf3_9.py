
def special_reverse(s, c):
  return ' '.join([''.join(reversed(x)) if x[0]==c else x for x in s.split()])

