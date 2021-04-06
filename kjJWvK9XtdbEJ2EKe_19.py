
def sort_array(lst):
    loop = 0
    result = []
    while len(lst) != 0:
        lowest = lst[0]
        loop = 0
        for i in lst:
            if lowest >= i:
                lowest = i
                lowestLoop = loop
            loop = loop + 1
        lst.pop(lowestLoop)
        result.append(lowest)
    return result;

