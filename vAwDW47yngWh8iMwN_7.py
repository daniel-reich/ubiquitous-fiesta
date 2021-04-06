
def cap_last(s):
  r = ""
  for w in s.split():
    r += w[:-1] + w[-1].upper() + " "
  return r[:-1]

