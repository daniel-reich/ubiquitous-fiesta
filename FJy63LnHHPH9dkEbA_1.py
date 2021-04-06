
import numpy
from decimal import *
​
def how_close_to_c(rapidity):
    
    sech = Decimal(1)/Decimal(numpy.cosh(2*rapidity))
    return "{:.2e}" .format(sech)

