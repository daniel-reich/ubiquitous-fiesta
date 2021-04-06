
def move_zeros(lst):
  n = [i for i in lst if i != 0 or i is False]
  z = [i for i in lst if i == 0 and i is not False]
  return n+z

