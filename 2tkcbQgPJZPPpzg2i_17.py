
def sum_of_holes(N):
  holes = {'0':1, '4':1, '6':1, '8':2, '9':1}
  hole_count = 0
  for i in range(1, N+1):
    x= str(i)
    for j in x:
      if j in holes:
        hole_count += holes[j]
  return hole_count

