
def left_rotations(st):
    return [st[i:] + st[:i] for i in range(len(st))]
  
​
def right_rotations(st):
    l = []
    for i in range(len(st)):
        l.append(st)
        st = st[-1] + st[:-1]
    return l

