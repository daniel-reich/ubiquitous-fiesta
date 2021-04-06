
def find_missing(lst):
    if lst == None:
        return False
    for i in range(len(lst)-1):
        if lst[i] == []:
            return False
    lst = sorted(lst, key=len)
    for i in range(len(lst)-1):
        increment = 1
        if len(lst[i]) + increment != len(lst[i+1]):
            return len(lst[i+1])-increment
    return False

