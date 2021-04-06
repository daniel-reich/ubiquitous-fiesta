
def farey(n):
    r = ["0/1", "1/1"]
    for x in range(1, n):
        for y in range(n, x, - 1):
            k = any([x % i == y % i == 0 for i in range(2, y + 1)])
            if x != y and not k:
                add = str(x) + "/" + str(y)
                r.append(add)
    return sorted(r, key=lambda x : eval(x))

