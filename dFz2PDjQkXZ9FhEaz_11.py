
def letter_check(lst):
  lst[0] = lst[0].lower()
  lst[1] = lst[1].lower()
  lst1 = list(lst[0])
  lst2 = list(lst[1])
  for i in lst2:
    if i not in lst1:
      return False
  return True

