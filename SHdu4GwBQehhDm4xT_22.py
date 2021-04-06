
def swap(lst):
    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = 0
        elif lst[i] == 0:
            lst[i] = 2
    for i in range(len(lst)):
        if lst[i] == 2:
            lst[i] = 1
    return lst
​
def freed_prisoners(prison):
    if prison[0] == 0:
        return 0
    at = 0
    freed = 1
    while at < len(prison) - 1:
        for cell in range(at, len(prison)):
            if prison[cell] == 0:
                freed += 1
                at = cell + 1
                prison = swap(prison)
        else:
            return freed
    return freed

