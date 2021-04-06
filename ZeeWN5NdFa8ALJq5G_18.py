
def nearest_chapter(d: dict, p: int) -> str:
    keys = sorted(list(d.keys()))
    closest = []
​
    for i, key in enumerate(keys):
        if d[key] < p:
            continue
​
        if i - 1 >= 0:
            closest.append(key)
            closest.append(keys[i - 1])
            break
​
        else:
            return key
​
    a = closest[0]
    b = closest[1]
​
    if abs(p - d[a]) <= abs(p - d[b]):
        return a
​
    return b

