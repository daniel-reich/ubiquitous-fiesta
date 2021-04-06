
def slicer(string, slic):
    sl, ss = len(slic), len(string)
    i = string.index(slic[0])
    # forward slice
    if slic == ''.join(sorted(slic)):
        if slic in string:
            #contiguous
            if sl == 1: return '[' + str(i) + ']'
            if i == 0: return '[:' + (str(sl + i) if sl < ss else '') + ']'
            return '[{}:{}]'.format(i, sl + i)
        else:
            #separated
            gap = string.index(slic[1]) - i
            last = string.index(slic[-1])
            res = '[' if i == 0 else '[' + str(i)
            return res + ':' + (str(last+1) if last + gap < ss else '') + ':' + str(gap) + ']'
    # reverse slice
    rstr = string[::-1]
    if slic in rstr:
        #contiguous
        return '[' + (str(i) if i < ss - 1 else '') + ':' + (str(i-sl) if i - sl >= 0 else '') + ':-1]'
    else:
        #separated
        gap = i - string.index(slic[1])
        last = string.index(slic[-1])
        res = '[' if i == ss - 1 else '[' + str(i)
        return res + ':' + (str(last - 1) if last - 1 > gap else '') + ':-' + str(gap) + ']'

