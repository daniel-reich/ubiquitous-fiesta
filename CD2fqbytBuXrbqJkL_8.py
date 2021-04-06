
def can_build(txt1, txt2):
  txt1 = txt1.replace(" ","")
  txt2 = txt2.replace(" ","")
  s1 = set(txt1)
  d1 = {el:txt1.count(el) for el in txt1}
  s2 = set(txt2)
  d2 = {el:txt2.count(el) for el in txt2}
  if s1.issubset(s2):
    for el in txt1:
      if d1[el] > d2[el]:
        return False
    return True
  else:
    return False

