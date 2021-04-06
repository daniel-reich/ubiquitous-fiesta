
import re
from math import ceil
def drange(*args):
    r = max([len(i) for i in re.findall(r"\.(\d*)", str(args))]+[0])
    step, start = 1, 0
    if len(args)==3:
        start, end, step = args
    elif len(args)==2:
        start, end = args
    else:
        end = args[0]
    return tuple(round(start+step*i, r) for i in range(ceil((end-start)/step)))

