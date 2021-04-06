
def perimeter(lst):
    from math import sqrt
    lst.append(lst[0])
    a = 0
    for i in range(len(lst)-1):
        a += sqrt((lst[i][0] - lst[i + 1][0]) ** 2 + (lst[i][1] - lst[i + 1][1]) ** 2)
    return round(a, 2)

