
def swap_d(k, v, swapped):
    if swapped == True:
        return (dict(zip(v,k)))
    elif swapped == False:
        return (dict(zip(k,v)))

