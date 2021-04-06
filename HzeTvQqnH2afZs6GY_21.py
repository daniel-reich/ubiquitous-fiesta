
def generate_rug(n, direction):
  def left(n):
    lst = []
    for i in range(n):
      lst.append(list(range(i, 0, -1)) + list(range(0, n - i)))
    return lst
​
  def right(n):
    lst = []
    for i in range(n):
      lst.append(list(range(n - 1 - i, 0, -1)) + list(range(0, i + 1)))
    return lst
    
  if direction == "left":
    return left(n)
  else: return right(n)

