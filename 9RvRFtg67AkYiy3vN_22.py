
def left_rotations(txt):
    return [txt[k:] + txt[:k] for k in range(len(txt))]
​
def right_rotations(txt):
    return [txt[-k:] + txt[:-k] for k in range(len(txt))]

