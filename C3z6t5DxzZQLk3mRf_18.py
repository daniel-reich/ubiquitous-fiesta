
def tune(lst):
    f = {0: 329.63, 1: 246.94, 2: 196, 3: 146.83, 4: 110, 5: 82.41}
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = ' - '
            continue
        e = round((lst[i] - f[i]) / f[i], 2)
        if e <= -0.03:
            lst[i] = '>>+'
        elif e < 0:
            lst[i] = '>+'
        elif e == 0:
            lst[i] = 'OK'
        elif e <= 0.02:
            lst[i] = '+<'
        else:
            lst[i] = '+<<'
    return lst

