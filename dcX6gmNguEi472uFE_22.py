
def double_factorial(num):
    fact=1
    if num%2==0:
        for i in range(2,num+1,2):
            fact=fact*i
        return fact
    else:
        for i in range(3,num+1,2):
            fact=fact*i
        return fact

