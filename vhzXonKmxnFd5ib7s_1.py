
import numpy 
def matrix_multiply(a, b):
    try:
        p=numpy.dot(a,b)
    except ValueError:
        return 'invalid'
    p=str(p).replace('  ',' ')
    p=p.replace(' ',', ')
    p=p.replace('[,','[')
    p=p.replace('\n','')
    return eval(p)

