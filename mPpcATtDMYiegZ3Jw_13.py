
def right_triangle(*n):
  lst = sorted([i for i in n])
  return lst[0]**2 + lst[1]**2 == lst[2]**2 if 0 not in lst and lst[0] > 0 else False

