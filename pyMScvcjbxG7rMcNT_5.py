
def dfs(L, s):
    for el in L:
        if type(el) == int:
            s += el
        else:
            s = dfs(el, s)
    return s
​
def sum_list(lst):
    return dfs(lst, 0)

