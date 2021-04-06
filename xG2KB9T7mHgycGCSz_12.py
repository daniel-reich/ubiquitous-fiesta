
def valid(txt):
  return len(txt) in [4,6] and all(x.isdigit() for x in txt)

