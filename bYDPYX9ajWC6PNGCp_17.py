
def track_robot(*steps):
  N = sum(steps[::4])
  E = sum(steps[1::4])
  S = sum(steps[2::4])
  W = sum(steps[3::4])
  return [E - W, N - S]

