
def track_robot(*steps):
  return [sum(steps[1::4])-sum(steps[3::4]),sum(steps[::4])-sum(steps[2::4])]

