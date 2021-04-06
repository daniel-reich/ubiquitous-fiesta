
def swap_d(k, v, swapped):
    if swapped == False:
        result = dict(zip(k, v))
    else:
        result = dict(zip(v, k))
​
    return result

