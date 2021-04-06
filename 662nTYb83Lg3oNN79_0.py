
def is_parallelogram(lst):
  A,B,C,D = sorted(lst)
  return slope(A,B)==slope(C,D) and slope(A,C)==slope(B,D)
​
def slope(A,B):
  return None if A[0]==B[0] else (A[1]-B[1])/(A[0]-B[0])

