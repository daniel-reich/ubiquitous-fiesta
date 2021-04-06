
def split(txt):
  v = "aeiou"
  txt1 = "".join(i for i in txt if i in v)
  txt2 = "".join(i for i in txt if not i in v)
  return txt1 + txt2

