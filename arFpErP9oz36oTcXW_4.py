
def secret(t):
  a,*b=t.split('.')
  return"<{0} class='{1}'></{0}>".format(a,' '.join(b))

