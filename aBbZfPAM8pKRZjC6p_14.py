
def fruit_salad(fruits):
    res = []
    for x in fruits:
        if len(x) % 2:
            res.append(x[:len(x) // 2])
            res.append(x[len(x) // 2:])
        else:
​
            res.append(x[:len(x) // 2])
            res.append(x[len(x) // 2:])
    return ''.join(sorted(res))

