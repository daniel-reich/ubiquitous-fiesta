
def trace(lst):
    sum = 0
    count = 0
    for el in lst:
        sum = sum + el[count]
        count = count + 1
    return sum

