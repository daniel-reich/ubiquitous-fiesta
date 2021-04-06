
def emphasise(txt):
  out = ""
  if len(txt) == 0:
    return ""
  txtSplit = txt.lower().split(" ")
  for w in txtSplit:
    l = list(w)
    l[0] = l[0].upper()
    out += "".join(l) + " "
  return out.strip()

