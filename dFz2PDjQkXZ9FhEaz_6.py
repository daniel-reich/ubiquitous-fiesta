
def letter_check(lst):
  return all(i in lst[0].lower() for i in lst[1])

