
def diamond(carat):
    ans = 'perfect cut'
    middle = int(carat / 2)
    erg = []
    for y in range(carat):
        erg.append([])
        for x in range(carat):
            if x == abs(middle - y) or x == (carat - 1) - abs(middle - y):
                erg[y].append(1)
            else:
                erg[y].append(0)
    if carat % 2 == 0:
        del erg[0]
        ans = 'good cut'
    return [erg, ans]

