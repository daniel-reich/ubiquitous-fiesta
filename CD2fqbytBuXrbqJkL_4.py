
def can_build(txt1, txt2):
  lst=[i for i in txt2]
  for j in txt1.replace(" ",""):
    if j in lst:
      lst.remove(j)
    else:
      return False
      exit()
  return True

