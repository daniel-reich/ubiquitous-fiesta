
def can_build(txt1, txt2):
  return all(txt1.count(x) <= txt2.count(x) for x in txt1 if x is not " ")

