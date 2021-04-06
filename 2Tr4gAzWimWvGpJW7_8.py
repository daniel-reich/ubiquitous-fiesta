
def is_there_consecutive(lst, n, times):
    if times == 0:
        return n not in lst
    elif times == 1:
        return n in lst
    else:
        target = [n] * times
        return any([lst[k:k+times] == target for k in range(len(lst) - times)])

