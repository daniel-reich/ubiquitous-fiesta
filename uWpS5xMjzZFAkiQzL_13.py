
def odds_vs_evens(num):
    evensum = 0
    oddsum = 0
    oddlist = []
    evenlist = []
    result = 'unknown'
    num = str(num)
    for digit in num:
        if digit in {'1', '3', '5', '7', '9'}:
            oddlist.append(digit)
        else:
            evenlist.append(digit)
​
    for item in oddlist:
        oddsum += int(item)
​
    for item in evenlist:
        evensum += int(item)
​
    if oddsum > evensum:
        result = "odd"
    elif evensum > oddsum:
        result = "even"
    else:
        result = "equal"
​
    return result

