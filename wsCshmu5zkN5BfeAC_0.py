
def divisible_by_left(n):
    n = str(n)
    res = [False]
    for i in range(1,len(n)):
        if int(n[i-1]) == 0 or int(n[i]) % int(n[i-1]) != 0:
            res.append(False)
        else:
            res.append(True)
    return res

