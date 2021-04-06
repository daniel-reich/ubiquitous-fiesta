
def total_volume(*boxes):
  return sum(i[0] * i[1] * i[2] for i in boxes)

