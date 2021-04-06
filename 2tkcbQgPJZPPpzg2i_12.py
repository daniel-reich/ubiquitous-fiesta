
def sum_of_holes(N):
  ans = 0
  holes = [0,4,6,8,9]
  for i in range(1,N+1):
    for c in range(len(str(i))):
      if int(str(i)[c]) in holes:
        if int(str(i)[c]) == 8:
          ans += 2
        else:
          ans += 1
  return ans

