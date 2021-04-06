
from itertools import permutations as perm
def greater_permutation(expr, nums):
    max=0
    p=perm(nums)
    for i in p:
        e=expr.replace('a',str(i[0]))
        e=e.replace('b',str(i[1]))
        e=e.replace('c',str(i[2]))
        if eval(e)>=max:
             max=eval(e)
             best=e
    if max==int(max):
        return best+' = '+str(int(max))
    return best+' = '+str(round(max,2))

