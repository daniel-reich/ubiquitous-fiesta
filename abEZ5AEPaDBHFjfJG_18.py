
def formula(txt):
  if not txt: return None
  a=4
  sides = txt.replace(" ","").replace("a","4").split("=")
  return len({eval(S) for S in sides}) == 1

