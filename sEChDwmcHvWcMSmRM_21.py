
def find_the_falsehoods(lst):
  lst1 = []
  for i in lst:
    if i == False or i == '' or i == [] or i == None or i == 0 or i == {} or i == ():
      lst1.append(i)
    else:
      continue
  return lst1

