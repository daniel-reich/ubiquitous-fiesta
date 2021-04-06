
def find_the_falsehoods(lst):
  false_lst = []
  for i in lst:
    if bool(i) == False:
      false_lst.append(i)
  return false_lst

