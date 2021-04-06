
from itertools import permutations
def simple_equation(a, b, c):
  nums=list(permutations([a,b,c],3))
  for i in nums:
      if i[0]+i[1]==i[2]:return '{}+{}={}'.format(i[0],i[1],i[2])
      if i[0]*i[1]==i[2]:return '{}*{}={}'.format(i[0],i[1],i[2])
      if i[0]/i[1]==i[2]:return '{}/{}={}'.format(i[0],i[1],i[2])
      if i[0]-i[1]==i[2]:return '{}-{}={}'.format(i[0],i[1],i[2])
  return ''

