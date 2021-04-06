
def persistence(num):
    count = 0
    accumulator = 1
    x = str(num)
    while len(x) != 1:
        for eachdigit in x:
            accumulator *= int(eachdigit)
        x = str(accumulator)
        accumulator = 1
        count += 1
    return count

