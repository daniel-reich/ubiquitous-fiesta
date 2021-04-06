
import numpy
def combinations(*items):
    result = filter(lambda x: x>0, items) 
    return numpy.prod(list(result))

