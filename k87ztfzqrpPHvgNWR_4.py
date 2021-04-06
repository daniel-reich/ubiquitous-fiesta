
def widen_streets(lst, n):
​
    lastrowlst = lst[len(lst) - 1].split()
    lastrowlen = len(lastrowlst)
    roadlocations = []
    offset = 0
    for x in range(lastrowlen - 1):
        location = len(lastrowlst[x]) + offset
        roadlocations.append(location)
        offset = location + 1
    roadlocations.reverse()
    finalarr = []
    for x in range(len(lst)):
        newstring = lst[x][:]
        for roadlocation in roadlocations:
            newstring =  newstring[:roadlocation] + (n * ' ') + newstring[roadlocation + 1:]
        finalarr.append(newstring)
    return finalarr

