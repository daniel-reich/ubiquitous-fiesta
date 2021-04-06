
def pairwise_swap(list_of_elements):
    odd = True
    newlst, a, top, val  = [], len(list_of_elements), 0, 0
    if a % 2 == 0: 
        for i in range(a):
            if odd:
                newlst += [list_of_elements[i+1]]
                odd = False
                continue
            else:
                newlst += [list_of_elements[i-1]]
                odd = True
        return newlst
    for i in range(a):
        if len(newlst) == len(list_of_elements) - 1:
            break
        if odd:
            newlst += [list_of_elements[i+1]]
            odd = False
            continue
        else:
            newlst += [list_of_elements[i-1]]
            odd = True   
    newlst.append(list_of_elements[-1])
    high = newlst[0]
    for i in str(newlst[0]):
        top += ord(i)
    for i in list_of_elements:
        for x in str(i):
            val += ord(x)
        if val == top:
            if newlst.count(high) > newlst.count(i):
                high = i
                continue
        if val > top:
            top = val
            high = i
        val = 0
    newlst[newlst.index(high)], newlst[-1] = newlst[-1], newlst[newlst.index(high)]
    return newlst

