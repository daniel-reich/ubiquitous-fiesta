
def total_overs(balls):
  balls_overs = str(balls//6) + "." + str(balls%6)
  if balls % 6 == 0:
    return balls/6
  return float(balls_overs)

