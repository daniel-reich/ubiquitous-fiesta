
def first_non_repeated_character(txt):
  for i in txt:
    if txt.count(i) == 1:
      return i
  return False

