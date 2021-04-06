
def reverse(txt):
  if len(txt)<1:return ''
  return txt[-1]+reverse(txt[:-1])

