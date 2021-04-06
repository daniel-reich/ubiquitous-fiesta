
def maskify(txt):
  txt2 = ""
  if len(txt) <= 4:
    return txt
  for i in range(0, len(txt) - 4):
    txt2 = txt2 + '#'
  txt2 = txt2 + txt[-4:]
  return txt2

