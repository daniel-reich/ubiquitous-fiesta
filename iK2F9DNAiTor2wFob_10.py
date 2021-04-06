
def calc(s):
  return ''.join(map(str, (map(ord, s)))).count('7') * 6

