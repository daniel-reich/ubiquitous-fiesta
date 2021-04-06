
def odd_sort(arr):
    if all(x % 2 == 0 for x in arr):
        return arr
    odds = sorted(x for x in arr if x % 2 != 0)
    temp = ['_' if x % 2 != 0 else x for x in arr]
    rep = ''
    while odds:
        for c in temp:
            if c == '_':
                rep += str(odds[0])
                odds.pop(0)
            else:
                rep += str(c)
    return list(map(int, rep))

