
def sum_every_nth(numbers, n):
    sum1=0
    lst=[0]+numbers
    for i in range(len(lst)):
        if i%n==0:
            sum1=sum1+lst[i]
    return sum1

