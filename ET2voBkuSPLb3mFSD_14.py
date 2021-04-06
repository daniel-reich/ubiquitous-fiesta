
def sum_every_nth(numbers, n):
    sum=0
    for i in range(n-1,len(numbers),n):
        sum+=numbers[i]
    return sum

