
import functools
def mystery_func(num):
    num = list(map(lambda x:int(x),list(str(num))))
    return functools.reduce(lambda a,b:a*b,num)

