
def wrap_around(txt, offset):
    '''
    Wraps around text by offset as per instructions
    '''
    size = len(txt)
​
    return ''.join(txt[(i+offset)%size] for i in range(size))

