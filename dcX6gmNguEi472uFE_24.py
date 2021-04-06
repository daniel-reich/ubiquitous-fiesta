
def double_factorial(num):
    if num==0 or num==1 or num==-1:
        return 1
    if num%2==0:
        a=2
        for i in range(2,num,2):
            a=a*(num+2-i)
    elif num%2!=0:
        a=1
        for i in range(1,num,2):
            a=a*(num+1-i)            
    return a

