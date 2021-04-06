
def is_narcissistic(n):
    no_of_digits=0
    num=n
    sum=0
    i=n
    while i>0:
        i=i//10
        no_of_digits+=1
    for j in range(no_of_digits):
        i=n%10
        n=n//10
        sum=sum+i**no_of_digits
    if sum==num:
        return True
    else :
        return False

