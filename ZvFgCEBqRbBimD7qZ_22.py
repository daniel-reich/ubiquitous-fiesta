
def bowling(pins, b=-1, f=1, sp=0, st=0):
  if not pins:
    return 0
​
  p = pins[0]
  s = p * (1 + sp + st)
  sp, st = st, 0
​
  if f == 10:
    return s + bowling(pins[1:], -1, f, sp, st)
  if b != -1:
    return s + bowling(pins[1:], -1, f + 1, sp + (b + p == 10), st)
  if p == 10:
    return s + bowling(pins[1:], -1, f + 1, sp, st + 1)
  return s + bowling(pins[1:], p, f, sp, st)

