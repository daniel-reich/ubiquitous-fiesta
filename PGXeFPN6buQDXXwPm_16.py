
def trace(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i][i]
    return sum

