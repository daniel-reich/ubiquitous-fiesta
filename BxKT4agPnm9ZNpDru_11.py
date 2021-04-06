
def zip_it(women, men):
  x = zip(women, men)
  if len(women) != len(men):
    return "sizes don't match"
  else:
    return list(x)

