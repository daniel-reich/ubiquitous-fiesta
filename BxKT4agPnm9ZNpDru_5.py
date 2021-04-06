
def zip_it(women,men):
  return "sizes don't match" if len(women) != len(men) else list(zip(women, men))

