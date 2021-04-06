
def bugger(num):
    prod = 1
    count = 0
    while len(str(num)) > 1:
        for digit in str(num):
            prod *= int(digit)
​
        num = prod
        count += 1
        prod = 1
    return count

