
def same_upsidedown(txt):
  new = ""
  for i in txt:
    if i == "6":
      new += "9"
    if i == "9":
      new += "6"
    if i == "0":
      new += "0"
  if txt == new[::-1]:
    return True
  else:
    return False

