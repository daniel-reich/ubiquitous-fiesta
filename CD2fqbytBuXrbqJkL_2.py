
def can_build(txt1, txt2):
  return all(txt1.count(i)<=txt2.count(i) for i in set([j for j in txt1 if j.isalnum()]))

