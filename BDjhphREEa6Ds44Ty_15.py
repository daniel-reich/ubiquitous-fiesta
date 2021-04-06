
def bomb(lst):
    distance1 = lst[0][2] * 0.343
    distance2 = lst[1][2] * 0.343
    distance3 = lst[2][2] * 0.343
    for i in range(51):
        for b in range(51):
            asquared = ((i-lst[0][0]) ** 2)
            bsquared = ((b-lst[0][1]) ** 2)
            csquared = round(distance1 ** 2)
            if asquared + bsquared == csquared:
                asquared = ((i-lst[1][0]) ** 2)
                bsquared = ((b-lst[1][1]) ** 2)
                csquared = round(distance2 ** 2)
                if asquared + bsquared == csquared:
                    asquared = ((i-lst[2][0]) ** 2)
                    bsquared = ((b-lst[2][1]) ** 2)
                    csquared = round(distance3 ** 2)
                    if asquared + bsquared == csquared:
                        return i, b

