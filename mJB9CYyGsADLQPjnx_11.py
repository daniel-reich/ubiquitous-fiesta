
def first_non_repeated_character(txt):
  for ch in txt:
    if ch.isalpha() and txt.count(ch)==1:
      return ch
  return False

