
def can_build(txt1, txt2):
  for i in list(txt1):
    if i!=' ' and txt1.count(i) > txt2.count(i): return False
  return True

