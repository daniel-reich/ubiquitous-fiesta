
def area_from_sides(a, b, c, p):
  return ((p/2) * (p/2 - a) * (p/2 - b) * (p/2 - c)) ** 0.5
​
def triangle(perimeter,area):
  retlst = []
  for s1 in range(perimeter // 3 + 1):
    for s2 in range(s1, perimeter // 2 + 1):
      s3 = perimeter - s1 - s2
      if s3 > s1 + s2:
        continue
      if s3 < s2:
        break
      if round(area_from_sides(s1, s2, s3, perimeter), 5) == area:
        retlst.append([s1, s2, s3])
  return retlst

