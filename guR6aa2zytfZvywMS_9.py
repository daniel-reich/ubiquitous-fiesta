
def total_overs(balls):
  balls1 = balls - (balls%6)
  if balls%6 == 0:
    return balls/6
  else:
    over = (((balls%6)/10) + ((balls1)/6))
    return over

