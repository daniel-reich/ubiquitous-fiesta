
def get_items_at(arr, par, res=None):
    if res is None:
        res = []
    if arr:
        if par == "even" and len(arr) > 1:
            res.append(arr[-2])
        elif par == "odd":
            res.append(arr[-1])
        arr = arr[:-2]
    return get_items_at(arr, par, res) if arr else res[::-1]

