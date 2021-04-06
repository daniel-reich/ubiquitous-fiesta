
def check_pattern(lst, pattern):
    d = {}
    for i in list(zip(pattern, lst)):
        if i[0] in d and d[i[0]] != i[1]:
            return False
        else:
            d[i[0]] = i[1]
    if len(set(list(map(tuple, d.values())))) != len(set(pattern)):
        return False
    return True

