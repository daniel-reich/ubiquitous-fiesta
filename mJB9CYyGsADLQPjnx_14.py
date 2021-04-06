
def first_non_repeated_character(txt):
  for n in range(len(txt)):
    if txt[n] not in txt[n+1:]:
      return txt[n]
    elif txt[n]==txt[n+1]:
      return False
  return False

