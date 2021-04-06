
def secret(txt):
  s = txt.split('.')
  s1 = "<{} class={}></{}>".format(s[0], "'"+' '.join(s[1:])+"'", s[0])
  return s1

