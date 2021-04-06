
def sle(m):
  a1 = m[0][0]
  b1 = m[0][1]
  c1 = m[0][2] * -1
  a2 = m[1][0]
  b2 = m[1][1]
  c2 = m[1][2] * -1
  if a1 / a2 != b1 / b2:
    x = (b1 * c2 - b2 * c1) // (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) // (a1 * b2 - a2 * b1)
    return (x, y)
  else:
    return False

