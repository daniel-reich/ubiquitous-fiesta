
def is_there_consecutive(lst, n, times):
    if times == 0:
        return n not in lst
    return str(n)*times in ''.join([str(x) for x in lst])

