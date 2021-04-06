
import itertools
def find_triangles(lst):
  dist = lambda p1, p2: (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2
  collinear = lambda p1, p2, p3: (p2[1]-p1[1]) * (p3[0]-p2[0]) == (p3[1]-p2[1]) * (p2[0]-p1[0])
​
  isoc = 0
  for a, b, c in itertools.combinations(lst,3):
    if not collinear(a,b,c):
      d = [dist(a,b), dist(a,c), dist(b,c)]
      if len(set(d)) == 2:
        isoc += 1
  return isoc

