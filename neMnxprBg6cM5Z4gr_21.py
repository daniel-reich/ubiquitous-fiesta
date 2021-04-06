
def arithmetic_progression(start, diff, n):
    listn = []
    start = start
    if diff<0:
        for i in range(1,n+1):
            listn.append(start)
            start -= abs(diff)
    elif diff>0:
        for i in range(start,n+1):
            listn.append(start)
            start += diff
​
    else:
        for i in range(start,n+1):
            listn.append(start)
    return ', '.join(str(numbers)for numbers in listn)

