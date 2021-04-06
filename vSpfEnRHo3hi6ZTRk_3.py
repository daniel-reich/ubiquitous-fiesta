
def free_throws(s, n):
  s = int(s[:-1])/100
  return str(round(s**n * 100)) + '%'

