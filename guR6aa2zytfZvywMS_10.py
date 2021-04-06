
def total_overs(balls):
  overs = balls // 6
  balls = (balls % 6) / 10.
  return overs + balls

