
import math
def find_vertex(x):
  s=''
  for j in x:
    if j!=' ':s+=j
  a,b,c=map(float,s.split('x'))
  return math.floor(-b/(2*a))

