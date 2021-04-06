
def bomb(txt):
  txt = txt.casefold()
  if "bomb" in txt:
    return "Duck!!!"
  else:
    return "There is no bomb, relax."

