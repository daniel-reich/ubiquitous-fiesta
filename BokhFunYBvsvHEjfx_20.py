
def seven_boom(lst):
  return 'Boom!' if any('7' in str(i) for i in lst) else 'there is no 7 in the list'

