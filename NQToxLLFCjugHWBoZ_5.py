
def sort_by_character(lst, n):
    dic = {}
    arr = []
    for x in lst:
        dic[x[n-1]] = x
    for key in sorted(dic.keys()):
        arr.append(dic[key])
    return arr

