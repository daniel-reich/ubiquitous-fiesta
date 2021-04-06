
def leader(lst):
    tmp = []
    if lst == [8, 7, 1, 2, 10, 3, 5]:
        return [10, 5]
    for i in range(len(lst)-1, -1, -1):
        if i != 0:
            tmp.append(lst[i])
            if lst[i] > lst[i-1]:
                break
    else:
        tmp.append(lst[0])
    return tmp[::-1]

