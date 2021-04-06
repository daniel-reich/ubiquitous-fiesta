
def letter_check(lst):
  return all([c in lst[0].lower() for c in lst[1].lower()])

