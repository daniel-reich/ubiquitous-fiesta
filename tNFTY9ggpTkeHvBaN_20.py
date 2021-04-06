
def total_volume(*boxes):
  prod = 1
  sum = 0
  for box in boxes:
    for x in box:
      prod *= x
    sum += prod
    prod = 1
  return sum

