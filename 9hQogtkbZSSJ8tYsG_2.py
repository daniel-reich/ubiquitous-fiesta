
def reverse(txt):
  return ''.join([i.lower() if i==i.upper() else i.upper() for i in txt])[::-1]

