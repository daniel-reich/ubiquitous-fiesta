
def can_build(txt1, txt2):
  return all(txt2.count(i) >= txt1.count(i) for i in set(txt1) if i.isalpha())

