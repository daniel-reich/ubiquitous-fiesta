
def letter_check(lst):
  for i in str.lower(lst[1]):
    if i not in str.lower(lst[0]):
      return False
  return True

