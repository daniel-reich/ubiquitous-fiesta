
import numpy as np
def printgrid(rows, cols):
    ar = np.arange(1,rows*cols+1)
    ar=  ar.reshape((cols,rows))
    return list(map(lambda x:list(x),ar.transpose()))

