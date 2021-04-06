
def first_non_repeated_character(txt):
  for t in txt.lower():
    if txt.count(t) == 1:
      return t
      
  return False

