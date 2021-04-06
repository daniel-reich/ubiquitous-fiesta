
def same_letter_pattern(a, b):
    dic1, dic2, res1, res2, x, y = dict(), dict(), "", "", 0, 0
    for i in a:
        if i not in dic1:
            dic1[i] = x
            x += 1
    for i in b:
        if i not in dic2:
            dic2[i] = y
            y += 1
    for i in a:
        res1 += str(dic1[i])
    for i in b:
        res2 += str(dic2[i])
    return res1 == res2

