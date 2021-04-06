
def reversible_inclusive_list(start,end):
    return list(range(start,end+1)) if start < end else list(range(end,start+1))[::-1]

