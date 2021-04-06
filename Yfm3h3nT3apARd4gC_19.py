
def rolls(lst):
    newlst = [lst[0]]
    for i,num in enumerate(lst[1:], 1):
        if lst[i-1]!=1:
            if lst[i-1]==6:
                newlst.append(num*2)
            else:
                newlst.append(num)
    return sum(newlst)

