
def normalize(a):
  if a.isupper():
    return a.lower().capitalize() + '!'
  elif not a.isupper():
    return a.capitalize()

