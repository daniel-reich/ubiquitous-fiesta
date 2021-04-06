
def slicer(string, slic):
    ind  = [string.index(x) for x in slic]
    if len(ind) == 1: return  str(ind)
    diff =  ind[-1] - ind[-2]
    start = '' if not ind[0] or ind[0]+1 == len(string) else str(ind[0])
    step = '' if diff == 1 else str(diff)
    if not ind[-1] or ind[-1]+diff >= len(string) or ind[-1] + diff < 0:
        end = '' 
    else:
        diff = 1 if diff >= 1 else -1
        end = str(ind[-1]+diff) 
    return '[{}:{}]'.format(start, end) if not step else '[{}:{}:{}]'.format(start, end, step)

