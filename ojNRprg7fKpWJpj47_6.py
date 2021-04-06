
import numpy as np
def shift_sentence(txt):
    a,b,c=[],[],[]
    for i in txt.split(' '):
        a.append(i[0])
    b=np.roll(a,1)
    for i,j in zip(txt.split(' '),b):
        c.append(j+i[1:])
    return (' '.join(c))

