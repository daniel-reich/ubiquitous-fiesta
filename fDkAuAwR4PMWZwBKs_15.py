
y = -1
def find_bob(names):
  counter = 0
  for x in names:
    if x == "Bob":
      return names.index(x)
      counter += 1
  if counter == 0:
    return y

