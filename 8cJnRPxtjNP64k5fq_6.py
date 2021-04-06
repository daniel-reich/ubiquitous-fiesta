
import numpy
​
def dance(lst, parameter):
  lst = numpy.array(lst)
  
  i = int(parameter == "men")
  lst[:, i] = lst[::-1, i]
  
  return lst.tolist()

