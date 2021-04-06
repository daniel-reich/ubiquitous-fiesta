
def dfs(L, ans):
    for el in L:
        if type(el) == list:
            ans = dfs(el, ans)
        else:
            ans += 1
    return ans
​
def get_length(lst):
    return dfs(lst, 0)

