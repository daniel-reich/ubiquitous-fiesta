
from math import ceil
def DECIMATOR(txt):
    return txt[:-1 * ceil(len(txt)*(1/10))]

