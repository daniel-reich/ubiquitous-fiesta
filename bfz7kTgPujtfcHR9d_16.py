
def x_pronounce(s):
  a = s.split()
  return" ".join("ecks"if i=="x"else i.replace("x","z")if i.startswith("x")else i.replace("x","cks")if"x"in i else i for i in a)

