
def seven_boom(lst):
  for number in lst:
    if '7' in str(number)[:]:
      return 'Boom!'
  return 'there is no 7 in the list'

