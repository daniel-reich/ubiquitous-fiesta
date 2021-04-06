
def will_fit(holds, cargo):
  d = {"S":50, "M":100, "L":200}
  h = sorted([d[i] for i in holds])
  hi = 0
  for i in cargo:
    while h[hi] < i:
      if hi + 1 == len(h):
        return False
      hi += 1
    h[hi] -= i
  return True

