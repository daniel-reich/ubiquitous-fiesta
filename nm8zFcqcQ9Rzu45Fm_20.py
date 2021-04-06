
def bridge_shuffle(lst1, lst2):
    if not lst1 and not lst2:
        return []
    elif not lst1:
        return lst2
    elif not lst2:
        return lst1
    result = [lst1[0], lst2[0]]
    for i in range(1, min(len(lst1), len(lst2))):
        result.append(lst1[i])
        result.append(lst2[i])
    if len(lst1) > len(lst2):
        result.extend(lst1[len(lst2):])
    else:
        result.extend(lst2[len(lst1):])
    return result

