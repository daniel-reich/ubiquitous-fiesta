
def flatten(r):
​
    def unnest(i):
        for e in i:
            if type(e) != list: res.append(e)
            else: unnest(e)
​
    res = []
    for i in r:
        if type(i) == list: unnest(i)
        else: res.append(i)
    return res

