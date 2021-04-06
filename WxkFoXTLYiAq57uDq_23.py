
def find_and_remove(dct):
    prim_keys = {k: {} for k in dct}
​
    for entry in dct:
        for k, v in dct[entry].items():
            if v.isdigit():
                prim_keys[entry][k] = int(v)
​
    return prim_keys

