
def uncensor(txt, vowels):
  txtLst = []
  txtLst[:] = txt
  txt = ""
  for i in txtLst:
    if i == "*":
      t = vowels[0]
      vowels = vowels[1:]
    else:
      t = i
    txt += t
  return txt

