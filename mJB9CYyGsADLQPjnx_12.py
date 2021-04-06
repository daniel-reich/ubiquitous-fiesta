
def first_non_repeated_character(txt):
  lst = [txt.count(i) for i in txt.lower()]
  try:
    return txt[(lst.index(1))]
  except ValueError:
    return False

