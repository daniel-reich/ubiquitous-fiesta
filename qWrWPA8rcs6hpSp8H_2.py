
from itertools import permutations
from functools import reduce
def determinant(A):
  fact = [reduce(lambda a,b:a*b,range(1,i+2)) for i in range(len(A)-1) if i%2]
  return sum([reduce(lambda a,b:a*b,[A[i][i2] for i,i2 in enumerate(p)]) \
    * [1, -1][(sum([ip//f for f in fact])+ip)%2] for ip,p in enumerate(permutations(range(len(A))))])

