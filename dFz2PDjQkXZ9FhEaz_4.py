
def letter_check(lst):
  result = True
  for i in lst[1].lower():
    if i not in lst[0].lower():
      result = False
  return result

