
def add(char, txt):
  lst = txt.split(' ')
  s = ''
  for i in lst:
    s += i + str(char)
  return s[:-1]

