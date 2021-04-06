
def yahtzee_score_calc(lst):
    points = [0] * 13
    points[0] += lst[0].count(1)
    points[1] += lst[1].count(2) * 2
    points[2] += lst[2].count(3) * 3
    points[3] += lst[3].count(4) * 4
    points[4] += lst[4].count(5) * 5
    points[5] += lst[5].count(6) * 6
    for p in set(lst[6]):
        if lst[6].count(p) >= 3:
            points[6] += sum(lst[6])
    for p in set(lst[7]):
        if lst[7].count(p) >= 4:
            points[7] += sum(lst[7])
    set_8 = set(lst[8])
    if len(set_8) == 2 and sum(lst[8].count(p) for p in set_8) == 5:
        points[8] += 25
    str_9 = ''.join(str(digit) for digit in sorted(lst[9]))
    if '1234' in str_9 or '2345' in str_9 or '3456' in str_9:
        points[9] += 30
    str_10 = ''.join(str(digit) for digit in sorted(lst[10]))
    if '12345' in str_10 or '23456' in str_10:
        points[10] += 40
    if len(set(lst[11])) == 1:
        points[11] += 50
    points[12] += sum(lst[12])
    return sum(points) + 35 if sum(points[:6]) >= 63 else sum(points)

