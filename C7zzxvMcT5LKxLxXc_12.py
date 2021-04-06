
def decode(txt):
  return [sum(int(i) for i in str(ord(j))) for j in txt]

