
factorial = {0: 1, 1: 1}
for k in range(2, 101):
    factorial[k] = k * factorial[k - 1]
​
def dfs(L, ans):
    ans *= factorial[len(L)]
    for el in L:
        if type(el) == list:
            ans = dfs(el, ans)
    return ans
​
def nespers(lst):
    return dfs(lst, 1)

