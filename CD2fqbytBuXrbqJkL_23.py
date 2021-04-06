
def can_build(txt1, txt2):
  return all(txt1.count(l)<=txt2.count(l) for l in txt1 if l!=" ")

