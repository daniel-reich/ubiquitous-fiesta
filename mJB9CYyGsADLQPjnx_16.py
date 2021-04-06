
def first_non_repeated_character(txt):
  txt = list(txt)
  non_repeated = []
  for letter in txt:
    if txt.count(letter) == 1:
      return letter
      non_repated.append(letter)
  if not non_repeated:
    return False

