
def solve(a, b):
  left_side, right_side = a - b, 4 + b - (3 * a)
​
  if not left_side and not right_side:
    return "Any number"
  elif not left_side and right_side:
    return "No solution"
  else:
    return round(right_side / left_side, 3)

