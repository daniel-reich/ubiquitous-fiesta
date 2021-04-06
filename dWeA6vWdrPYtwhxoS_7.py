
def dfs(L, cnt):
    for item in L:
        if type(item) in [int, float]:
            cnt += 1
        elif type(item) == list:
            cnt = dfs(item, cnt)
    return cnt
​
def count_number(lst):
    return dfs(lst, 0)

