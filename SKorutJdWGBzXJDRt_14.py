
def greet_people(names):
  s = ["Hello "]
  z = []
  for x in names:
    for y in s:
      z.append(y+x)
  return ", ".join(z)

