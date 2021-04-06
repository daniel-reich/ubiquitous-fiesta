
#just math, but it was fun A(n) = 10A(n-1) + (10**n)*(9/2)
​
def sum_digits_in_range(n):
    n=int(n)
    return n*10**n*9//2

