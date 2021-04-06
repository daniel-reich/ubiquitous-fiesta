
def special_reverse(s, c):
  return ' '.join([x[::-1] if x[0]==c else x for x in s.split(' ')])

