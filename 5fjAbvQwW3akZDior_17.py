
def unrepeated(txt):
  txt1 = ""
  for i in txt:
    if i not in txt1:
      txt1 += i
  return txt1

