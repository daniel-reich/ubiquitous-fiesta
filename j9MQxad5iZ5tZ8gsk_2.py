
import re
def find_vertex(s):
  p=r'\-?\d+(?=x)'
  A=[eval(x) for x in re.findall(p,s)]
  res='-{1}//(2*{0})'.format(*A)
  return eval(res)

