
def find_and_remove(dct):
    for key in dct:
        result = {}
        for key_inner in dct[key]:
           if dct[key][key_inner].isdecimal():
              result[key_inner] = int(dct[key][key_inner])
        dct[key] = result
    return dct

