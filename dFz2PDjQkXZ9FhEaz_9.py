
def letter_check(lst):
  return all(x in lst[0].lower() for x in lst[1])

