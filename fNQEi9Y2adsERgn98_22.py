
def line(a, b):
  return (((a[0] - b[0])**2) + ((a[1] - b[1])**2)) ** 0.5
def perimeter(lst):
  return round(line(lst[0],lst[1]) + line(lst[0],lst[2]) + line(lst[1],lst[2]), 2)

