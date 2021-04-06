
def is_autobiographical(n):
  s = str(n)
  return n >= 0 and len(s)<11 and\
  all(s.count(str(x))==int(s[x]) for x in range(len(s)))

