
def right_triangle(x, y, z):
  lst = sorted([x, y, z])
  cat1 = lst[0]
  cat2 = lst[1]
  hip = lst[2]
  return all(n > 0 for n in lst) and hip**2 == cat1**2 + cat2**2

