
def can_build(txt1, txt2):
  txt1 = txt1.replace(" ","")
  txt2 = txt2.replace(" ","")
  for x in txt1:
    if txt1.count(x) > txt2.count(x):
      return False
  return True

