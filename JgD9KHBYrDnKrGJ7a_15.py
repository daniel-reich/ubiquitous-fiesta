
def swap_dict(adict):
    empty_dict = {}
    for eachkey in adict:
        empty_dict[adict[eachkey]] = []
    for eachkey in adict:
        empty_dict[adict[eachkey]].append(eachkey)
    return empty_dict

