
def first_non_repeated_character(txt):
  for letter in txt:
    if txt.count(letter) == 1:
      return letter
  return False

