
def bridge_shuffle(lst1, lst2):
    result = []
    i = 0
    
    while i < max(len(lst1),len(lst2)):
        if i < len(lst1):
            result.append(lst1[i])
        if i < len(lst2):
            result.append(lst2[i])
        i += 1
    return result

