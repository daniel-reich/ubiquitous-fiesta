
def func(lst, ans=0):
    ans += len(lst)
    for el in lst:
        if type(el) == list:
            ans = func(el, ans)
    return ans

