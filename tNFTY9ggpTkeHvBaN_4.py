
def total_volume(*boxes):
  x = 0
  for i in boxes:
    x = x + (i[0]*i[1]*i[2])
  return x

