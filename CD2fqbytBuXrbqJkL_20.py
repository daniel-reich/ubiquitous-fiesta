
def can_build(txt1, txt2):
  for i in txt1:
    if i != ' ' and i not in txt2:
      return False
    txt2 = txt2.replace(i,'',1)
  return True

