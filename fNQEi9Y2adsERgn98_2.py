
def perimeter(lst):
  get_dist = lambda a,b: pow(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2), .5)
  p1,p2,p3 = lst
  return round(sum(get_dist(*c) for c in [(p1,p2), (p1,p3), (p2,p3)]), 2)

