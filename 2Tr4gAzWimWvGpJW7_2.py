
def is_there_consecutive(lst, n, times):
​
    if not times:
        return not n in lst
​
    return str(n) * times in ''.join(map(str, lst))

