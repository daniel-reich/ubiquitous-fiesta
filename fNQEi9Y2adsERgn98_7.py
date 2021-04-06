
def perimeter(lst):
    return round(pow(pow(lst[1][0] - lst[0][0], 2) +
                     pow(lst[1][1] - lst[0][1], 2), 0.5) +
                 pow(pow(lst[2][0] - lst[1][0], 2) +
                     pow(lst[2][1] - lst[1][1], 2), 0.5) +
                 pow(pow(lst[2][0] - lst[0][0], 2) +
                     pow(lst[2][1] - lst[0][1], 2), 0.5)
                 , 2)

