
def cap_last(txt):
  s = ''
  for i in txt.split():
    s += i[:-1] + i[-1].upper() + ' '
  return s[:-1]

