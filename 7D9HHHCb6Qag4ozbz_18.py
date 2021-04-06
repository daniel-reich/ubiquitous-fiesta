
def find_zip(txt):
  z1 = txt.find("zip")
  z2 = txt[z1+3:].rfind("zip")
  if z2 != -1:
    z2 += z1 + 3
  return z2

