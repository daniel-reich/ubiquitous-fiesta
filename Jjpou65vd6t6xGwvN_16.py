
def get_case(txt):
  if txt.islower():
    return "lower"
  elif txt.isupper():
    return "upper"
  else:
    return "mixed"

