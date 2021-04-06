
from functools import  reduce
def primorial(n):
     p = [2,3,5,7,11,13,17,19,23]
     return reduce(lambda a,b:a*b,p[:n])

