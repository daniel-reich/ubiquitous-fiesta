
def get_items_at(arr, par, ans=[], first=True):
    if first:
        ans = []
    n = len(arr)
    if ans == [] and par == "even":
        arr.pop()
    if len(arr) == 0:
        return ans[::-1]
    ans.append(arr[-1])
    return get_items_at(arr[:-2], "odd", ans, False)

