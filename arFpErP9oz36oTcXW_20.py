
def secret(txt):
  s = txt.split('.')
  s1, s2 = s[0], ' '.join(s[1:])
  return "<{0} class='{1}'></{0}>".format(s1,s2)

