
def left_rotations(txt):
    result = []
    for i in range(len(txt)):
        result.append(txt[i:] + txt[:i])
    return result
​
​
def right_rotations(txt):
    result = []
    for i in range(len(txt),0,-1):
        result.append(txt[i:] + txt[:i])
    return result

