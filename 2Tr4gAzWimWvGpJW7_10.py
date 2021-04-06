
def is_there_consecutive(lst, n, times):
    c = []
    for i in lst:
        if i == n:
            c += [i]
        elif len(c) == times:
            return True
        else:
            c = []
    return False

