
def count_repetitions(lst):
    res = {}
    for i in lst:
        if i not in res: res[i] = lst.count(i)
    return res

