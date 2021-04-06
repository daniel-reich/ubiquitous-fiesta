
def first_non_repeated_character(txt):
  for char in txt:
    if txt.count(char) == 1:
      return char
  
  return False

