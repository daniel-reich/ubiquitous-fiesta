
def every_some(test, val, a, b, c, d, e):
    arr = [a, b, c, d, e]
    if val == "everybody":
        return all(eval(str(x) + test) for x in arr)
    else:
        return any(eval(str(x) + test) for x in arr)

