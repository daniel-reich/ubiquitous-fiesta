
def alphabet_index(txt):
  return " ".join(str(ord(l)-64) for l in txt.upper() if l.isalpha())

