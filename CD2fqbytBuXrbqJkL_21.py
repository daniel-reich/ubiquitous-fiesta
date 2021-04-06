
def can_build(txt1, txt2):
  new = []
  if len(txt1)<=len(txt2):
    d1 = {i: txt1.count(i) for i in sorted(txt1.replace(' ', ''))}
    d2 = {i: txt2.count(i) for i in sorted(txt2.replace(' ', ''))}
    for i in d1:
      if d1[i] <= d2[i]:
        new.append(i)
    if len(d1) == len(new):
      return True
    else:
      return False
  else:
    return False

