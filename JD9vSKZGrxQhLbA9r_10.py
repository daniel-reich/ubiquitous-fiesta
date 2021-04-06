
from decimal import *
def pile_of_cubes(m):
  if m>100:
    a=(Decimal(8*Decimal(m).sqrt()+1).sqrt()-1)/2
    if a%1==0:return a

