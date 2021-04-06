
def move(mat):
  def f(to):
    if to == "up":    return move(mat[1:] + mat[:1])
    if to == "down":  return move(mat[-1:] + mat[:-1])
    if to == "left":  return move([r[1:] + r[:1] for r in mat])
    if to == "right": return move([r[-1:] + r[:-1] for r in mat])
    return mat
  return f

