
def invert(s):
  return ''.join([x.lower(), x.upper()][x.islower()] for x in s[::-1])

