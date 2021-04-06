
def last_dig(a, b, c):
    for i in range(0,1):
        x=a%10
        y=b%10
        z=x*y
        k=z%10
        d=c%10
        if k==d:
            return True
        else:
            return False

