
def numbers_to_ranges(lst):
    if lst == []:
        return []
    result = []
    lst.sort()
    sublist = [lst[0]]
    for i in range(0,len(lst)):
        if i != 0:
            if lst[i]-1 == sublist[-1]:
                sublist.append(lst[i])
            else:
                if len(sublist) == 1:
                    result.append(str(sublist[0]))
                else:
                    result.append(str(sublist[0])+"-"+str(sublist[-1]))
                sublist = [lst[i]]
    if len(sublist) == 1:
        result.append(str(sublist[0]))
    else:
        result.append(str(sublist[0])+"-"+str(sublist[-1]))
    return result

