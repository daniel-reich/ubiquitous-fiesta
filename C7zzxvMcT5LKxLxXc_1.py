
def decode(txt):
  return [sum(map(int,str(ord(c)))) for c in txt]

