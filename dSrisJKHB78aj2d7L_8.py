
from math import sin,pi,acos
def triangle(perimeter,area):
  lst = []
  for a in range(1,perimeter-1):
    for b in range(1,a+1):
      c = perimeter-a-b
      if(c>0):
        A,B,C = angles(a,b,c)
        h = a*sin(C)
        if round((b*h)/2,5) == area and sorted([a,b,c]) not in lst:
          lst.append(sorted([a,b,c]))
  lst = sorted(lst,key = lambda x:x[0])
  return lst
      
def angles(a,b,c):
  try:
    A = acos((b**2+c**2-a**2)/(2*b*c))
    B = acos((c**2+a**2-b**2)/(2*c*a))
    C = acos((a**2+b**2-c**2)/(2*a*b))
  except:
    A,B,C = 1,1,1
  return [A,B,C]

