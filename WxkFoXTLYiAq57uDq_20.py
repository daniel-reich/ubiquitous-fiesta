
def find_and_remove(dct):
    for k1, v1 in dct.items():
        temp_dict = {}
        for k2, v2 in v1.items():
            if v2.isdigit(): temp_dict[k2] = int(v2)
        dct[k1] = temp_dict
    return dct

