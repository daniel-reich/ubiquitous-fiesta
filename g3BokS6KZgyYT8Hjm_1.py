
def shift_to_left(x, y, z=1):
  if y == 0:
    return x * z
  return shift_to_left(x, y-1,z*2)

