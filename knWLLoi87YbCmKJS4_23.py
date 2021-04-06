
def happy(n):
    s = 0
    while(n!=0):
        r = n % 10
        s = s + r**2
        n=n//10
    if(s==4):
        return False
    elif(s==1):
        return True
    else:
        return happy(s)

