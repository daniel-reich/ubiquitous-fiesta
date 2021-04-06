
def letter_check(lst):
  for i in lst[1].lower():
    if i not in lst[0].lower():
      return False
  return True

