
def letter_check(lst):
  for i in range(len(lst)):
    lst[i] = lst[i].lower()
  for item in lst[1]:
    if item not in lst[0]:
      return False
  return True

