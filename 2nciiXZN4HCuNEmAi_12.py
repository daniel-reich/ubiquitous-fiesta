
def flatten(r, ans = [], new = True):
    if new:
        ans = []
    for el in r:
        if type(el) == list:
            ans = flatten(el, ans, False)
        else:
            ans.append(el)
    return ans

