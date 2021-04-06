
def first_non_repeated_character(txt):
  for i in range (len(txt)):
    if (txt.count(txt[i])==1):
      return txt[i]
  return False

