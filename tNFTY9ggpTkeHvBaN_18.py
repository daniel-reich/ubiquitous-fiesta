
import functools
def total_volume(*boxes):
    ls = [a for a in boxes]
    return sum([functools.reduce(lambda x,y:x*y,a) for a in ls])

