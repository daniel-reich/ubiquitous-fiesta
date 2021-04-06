
def bug_jump(h0, t):
  v0 = 2 * h0**0.5
  t /= 1000
  h = round(v0*t - t*t, 2)
  return [0, None] if h < 0 else [h, 'down' if v0 - 2*t < 0 else 'up']

