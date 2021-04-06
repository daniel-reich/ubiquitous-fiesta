
def validate_spelling(txt):
  txt = "".join(c for c in txt.upper() if c.isalpha() or c == " ")
  w = txt.split()
  return "".join(w[:-1]) == w[-1]

