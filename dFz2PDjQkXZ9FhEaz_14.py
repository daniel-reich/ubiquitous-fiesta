
def letter_check(lst):
  for letter in lst[1].lower():
    if not letter in lst[0].lower():
      return False
  return True

