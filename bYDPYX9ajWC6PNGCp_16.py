
def track_robot(*steps):
  ver = sum(steps[::4]) - sum(steps[2::4])
  hor = sum(steps[1::4]) - sum(steps[3::4])
  return [hor,ver]

