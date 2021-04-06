
def decode(txt):
  return [sum(int(x) for x in str(ord(i))) for i in txt]

