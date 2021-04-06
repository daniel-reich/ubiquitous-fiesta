
def reversible_inclusive_list(start, end,res=''):
    if start>end:
        return [start]+[i for i in range(end,start)][::-1]
    else:
        return [i for i in range(start,end)]+[end]

