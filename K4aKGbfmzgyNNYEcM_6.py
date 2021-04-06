
def is_shape_possible(n, angles):
    flag=1
    if n<3:
        flag=0
    elif (n-2)*180!=sum(angles):
        flag=0
    else:
        for i in angles:
            if i>=180:
                flag=0
    return flag

