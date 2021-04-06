
import numpy
def digital_division(n):
  passed = 0
  if not sum([n%x for x in map(int,str(n)) if x!=0]): passed+= 1
  s = sum(map(int,str(n)))
  if s != 0: 
    if not n % s: passed += 1
  p = numpy.prod([x for x in map(int,str(n))])
  if p != 0: 
    if not n % p : passed +=1
  return "Perfect" if passed ==3 else passed if 0<passed<3 else "Indivisible"

