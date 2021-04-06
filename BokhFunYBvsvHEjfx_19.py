
def seven_boom(lst):
  for num in lst:
    num = str(num)
    if '7' in num:
      return "Boom!"
  return "there is no 7 in the list"

