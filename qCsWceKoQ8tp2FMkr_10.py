
def is_triangle(a, b, c):
  lst = sorted([a,b,c])
  return lst[-1] < sum(lst[:-1])

