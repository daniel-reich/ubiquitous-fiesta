
def first_non_repeated_character(txt):
  for c in txt:
    if txt.count(c) == 1:
      return c
  return False

