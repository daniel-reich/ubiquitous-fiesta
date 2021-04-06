
from collections import deque
def left_rotations(txt):
    DQ = deque(txt)
    L = []
    L.append(''.join(DQ))
    for i in range(len(txt)-1):
        DQ.rotate(-1)
        L.append(''.join(DQ))
    print(L)
    return L
​
def right_rotations(txt):
    DQ = deque(txt)
    L = []
    L.append(''.join(DQ))
    for i in range(len(txt)-1):
        DQ.rotate(1)
        L.append(''.join(DQ))
    print(L)
    return L

