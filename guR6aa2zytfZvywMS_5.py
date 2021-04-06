
def total_overs(balls):
  over = int(balls / 6)
  remaining_balls = balls % 6
  return over + remaining_balls / 10

