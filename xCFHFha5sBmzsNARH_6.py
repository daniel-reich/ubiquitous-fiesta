
def reverse(txt):
  if len(txt)==0:
    return ''
  else:
    return txt[-1]+reverse(txt[:-1])

