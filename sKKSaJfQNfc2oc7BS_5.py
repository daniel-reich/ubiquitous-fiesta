
def sle(m):
  a, b, c, d, e, f = m[0][0], m[0][1], m[0][2], m[1][0], m[1][1], m[1][2]
  if d/e == a/b or e/d == b/a:
    return False
  return (round((f/e - c/b) / (d/e - a/b)), round((f/d - c/a) / (e/d - b/a)))

