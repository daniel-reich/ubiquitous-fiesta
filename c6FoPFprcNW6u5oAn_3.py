
def farey(n):
    f = {}
    for denom in reversed(range(1, n+1)):
        for num in range(denom+1):
            f[float(num)/denom] = "{}/{}".format(num, denom)
​
    return [f[k] for k in sorted(f.keys())]

