
def sum_fractions(lst):
    sum = 0
    for sublst in lst:
        sum += sublst[0] / sublst[1]
    return round(sum, 0)

