
def is_there_consecutive(lst, n, times):
    return str(n)*times in ''.join(map(str, lst))

