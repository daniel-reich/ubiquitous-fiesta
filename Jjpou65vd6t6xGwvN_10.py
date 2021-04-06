
def get_case(txt):
  if txt.lower() == txt:
    return "lower"
  elif txt.upper() == txt:
    return "upper"
  else:
    return "mixed"

