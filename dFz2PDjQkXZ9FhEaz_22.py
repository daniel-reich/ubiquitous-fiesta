
def letter_check(lst):
  i, j = lst
  for word in j:
    if not word.lower() in i.lower():
      return False
  return True

