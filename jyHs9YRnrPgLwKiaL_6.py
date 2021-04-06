
def split(x):
    if x < 5:
        return x
    lst = [pow((x / i), i) for i in range(1, x)]
    return round(sorted(lst)[-1], 1)

