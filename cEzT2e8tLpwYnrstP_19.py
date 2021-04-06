
def swap_d(k, v, swapped):
    if swapped == False: return {a:b for a,b in zip(k,v)}
    else: return {b:a for a,b in zip(k,v)}

