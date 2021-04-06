
def first_non_repeated_character(txt):
  if len(txt) is 1:
    return txt
  for x, char in enumerate(txt):
    if char not in txt[x+1:] and char != txt[x-1]:
      return char
  return False

