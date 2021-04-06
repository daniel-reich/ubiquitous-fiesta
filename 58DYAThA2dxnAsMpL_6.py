
def integer_boolean(n):
  things = []
  for statement in n:
    if statement == "1":
      things.append(True)
    if statement == "0":
      things.append(False)
  return things

