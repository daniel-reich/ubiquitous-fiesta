
def zip_it(women, men):
  if len(women)==len(men):
    lst=[]
    for i in range(len(women)):
      lst.append((women[i],men[i]))
    return lst
  else:
    return "sizes don't match"

