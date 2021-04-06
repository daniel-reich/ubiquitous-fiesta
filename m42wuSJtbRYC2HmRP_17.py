
from math import log
def largest_exponential(lst):
    return sorted([[i[1]*log(i[0]), lst.index(i)+1] for i in lst])[-1][-1]

