
def normalize(txt):
  c = [x.isupper() for x in txt if x.isalpha()]
  f = lambda x, i: x.lower() if i else x.upper()
  return ''.join([f(x, i) for i, x in enumerate(txt)]) + '!' if all(c) else txt

