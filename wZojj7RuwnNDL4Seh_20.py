
def completely_filled(lst):
  for st in lst:
    for letter in st:
      if letter==" ":
        return False
  return True

