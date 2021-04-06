
def reverse(txt):
  return ' '.join((x if len(x)<5 else x[::-1]) for x in txt.split())

