
from itertools import combinations
def find_triangles(lst):
  side = lambda p1, p2: (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
​
  count = 0
  for perm in combinations(lst, 3):
    A, B, C = perm
    if (B[1] - A[1]) * (C[0] - A[0]) != (C[1] - A[1]) * (B[0] - A[0]):
      s1, s2, s3 = side(A, B), side(B, C), side(C, A)
      if s1 == s2 or s2 == s3 or s3 == s1:
        count += 1
  return count

