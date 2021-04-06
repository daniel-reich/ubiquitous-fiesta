
def is_repeated(strn):
    repeat_idx = strn[1:].index(strn[0])+1
    repeat = strn[:repeat_idx]
    return strn.count(repeat) if strn.count(repeat)>1 else False

