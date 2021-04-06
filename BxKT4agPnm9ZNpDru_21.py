
def zip_it(women,men):
  if len(women) != len(men):
    return "sizes don't match"
  return list(zip(tuple(women), tuple(men)))

