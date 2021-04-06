
import numpy as np
def classify_rug(pattern):
    '''Symmetrical Patterns
    classify the array as: imperfect; horizontally symmetric; vertically symmetric; perfect'''
    a = np.array(pattern)
    
    hor = True
    for row in range(a.shape[0] // 2):
        if not np.array_equal(a[row], a[-row-1]):
            hor = False
            break
​
    ver = True
    for col in range(a.shape[1] // 2):
        if not np.array_equal(a[:,col], a[:,-col-1]):
            ver = False
            break 
​
    if hor and ver: return 'perfect'
    if hor: return 'horizontally symmetric'
    if ver: return 'vertically symmetric'
    return 'imperfect'

