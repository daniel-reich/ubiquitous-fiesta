
def zip_it(women, men):
  if len(women) != len(men):
    return "sizes don't match"
  elif len(women) == len(men):  
    return list(zip(women, men))

