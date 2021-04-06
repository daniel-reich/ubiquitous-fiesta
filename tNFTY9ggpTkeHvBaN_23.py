
def total_volume(*boxes):
  sum = 0
  for item in boxes:
    total = 1
    for sisi in item:
      total *= sisi
    sum += total
  return sum

