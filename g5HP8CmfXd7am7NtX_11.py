
def keyboard_mistakes(txt):
  x = txt.maketrans("0145","OIAS")
  return txt.translate(x)

