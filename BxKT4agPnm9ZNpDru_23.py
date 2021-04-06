
def zip_it(women, men):
  lst = []
  if len(women) == len(men):
    for i in range(len(men)):
      lst.append(tuple([women[i], men[i]]))
    return lst
  return "sizes don't match"

