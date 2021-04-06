
def make_change(c):
  d = {}
  d["q"] = c // 25
  c -= 25 * d["q"]
  d["d"] = c // 10
  c -= 10 * d["d"]
  d["n"] = c // 5
  c -= 5 * d["n"]
  d["p"] = c
  return d

