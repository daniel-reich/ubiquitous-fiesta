
def on_rectangle_bounds(s):
  lb = min(x for x, y in s)
  rb = max(x for x, y in s)
  bb = min(y for x, y in s)
  ub = max(y for x, y in s)
  return all( x in (lb,rb) or y in (bb, ub) for x, y in s)

