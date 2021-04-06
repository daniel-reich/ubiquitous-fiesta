
#adapted from Vitosh Academy
#https://www.vitoshacademy.com/python-algorithms-maximum-combinations-of-coins/
def football(score):
  points = (0,2,3,6,7,8)
  p = [0]*(score+1)
  for point in points:
      for i in range(score+1):
          if point == i:
              p[i]+=1
          if i-point>0:
              p[i]=p[i]+p[i-point]
  return p[score]

