
def special_reverse(s, c):
  s = s.split(' ')
  return ''.join([(x+ ' ') if x[0] != c else (x[::-1] + ' ') for x in s])[0:-1]

