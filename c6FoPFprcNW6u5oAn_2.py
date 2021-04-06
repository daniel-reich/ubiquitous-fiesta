
from fractions import Fraction as fr
farey=lambda s:['0/1']+[str(x)for x in sorted({fr('%d/%d'%(i,j))for i in range(1,s)for j in range(1,s+1)if i<=j})][:-1]+['1/1']

