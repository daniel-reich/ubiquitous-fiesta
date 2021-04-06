
import itertools
import numpy
​
def product_pair(lst, k):
    max_value = 0
    min_value = 0
    outputlist = []
​
    if k > len(lst) or len(lst) == 0:
        return None
    elif k == len(lst):
        max_value = numpy.prod(lst)
        min_value = numpy.prod(lst)
    else:
        onetime = True
        for i in itertools.combinations(lst, k):
            if onetime == True:
                max_value = numpy.prod(i)
                min_value = numpy.prod(i)
                onetime = False
            answer = numpy.prod(i)
            if answer > max_value:
                max_value = answer
            elif answer < min_value:
                min_value = answer
    outputlist.append(min_value)
    outputlist.append(max_value)
    return tuple(outputlist)

