
def seven_boom(lst):
  for i in lst:
    a = str(i)
    if a.find('7') != -1:
      return 'Boom!'
  return "there is no 7 in the list"

