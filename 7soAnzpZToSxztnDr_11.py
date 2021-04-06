
def shift_left(x, y):
  # your recursive solution here
  if y == 0: return x
  elif y == 1: return x*2
  else:
      x *= 2
      y -= 1
      return shift_left(x, y)

