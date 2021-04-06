
def first_non_repeated_character(txt):
  if txt == "": return False
  for letter in txt:
    if txt.count(letter) == 1: return letter
  return False

