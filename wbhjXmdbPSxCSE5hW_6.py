
def sigilize(desire):
  return "".join(x for i, x in enumerate(desire.upper()) if x not in ' AEIOU' + desire.upper()[i+1:])

