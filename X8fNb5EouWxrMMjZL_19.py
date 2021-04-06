
def collatz(num):
    c=0
    while num > 1:
        if num%2==0:
            num=num/2
            c=c+1
        elif num%2!=0:
            num=num*3+1
            c=c+1
    return c

