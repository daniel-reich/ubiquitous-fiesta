
def emphasise(txt):
  a = txt.lower().split()
  txtStr = []
  for n in a:
    txtStr.append(n[0].upper()+n[1:])
  return " ".join(txtStr)

