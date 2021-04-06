
def find_and_remove(dct):
    [ndct,nv] = [{},{}]
    for key in dct.keys():
        for nkey in dct[key].keys():
            if dct[key][nkey].isdigit():nv[nkey]=int(dct[key][nkey])
        ndct[key]= nv
        nv={}
    return ndct

