
def calc_diff(obj, limit):
    summ = 0
    for i in obj:
        summ += obj[i]
    summ -= limit
    return summ

