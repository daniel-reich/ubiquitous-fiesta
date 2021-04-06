
def first_non_repeated_character(txt):
  if txt == "":
    return False
  for i in range(0, len(txt)):
    if txt[i] != " ":
      if txt.count(txt[i]) == 1:
        return txt[i]
        break
      else:
        if i == len(txt) - 1:
          return False

