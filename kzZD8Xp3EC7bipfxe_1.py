
d = {"zero": 0, "one": 1}
r = {0: "Zero", 1: "One", 2: "Two"}
def worded_math(equ):
  a, op, b = equ.lower().split()
  if op == "plus":
    return r[d[a] + d[b]]
  else:
    return r[d[a] - d[b]]

