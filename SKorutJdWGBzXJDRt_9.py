
def greet_people(names):
  for x, name in enumerate(names):
    names[x] = "Hello "+ name
  s = ", "
  return s.join(names)

