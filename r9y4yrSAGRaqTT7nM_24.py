
def find_missing(lst):
    if lst == None:
        return False
    else:
        lst.sort(key=len)
    if len(lst) == 0:
        return False
        quit();
    elif len(lst[0]) == 0:
        return False
    else:
        count = len(lst[0])
    for list in lst:
        if count != len(list):
            return count
        count += 1

