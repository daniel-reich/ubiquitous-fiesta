
def find_the_falsehoods(lst):
  new_lst = []
  for i in lst:
    if bool(i) == False:
      new_lst.append(i)
  return new_lst

