
def number_of_days(coordinate):
    ans = abs(coordinate[0]) + abs(coordinate[1])
    if ans <= 5:
        return ans
    if ans % 5 == 0:
        return ans + ans // 5 - 1
    return ans + ans // 5

