
def track_robot(*steps):
  s = lambda x: sum(steps[x::4])
  return [s(1)-s(3), s(0)-s(2)]

