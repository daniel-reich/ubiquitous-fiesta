
def last_dig(a, b, c):
    a1=a%10
    b1=b%10
    c1=c%10
    c2=a1*b1
    c3=c2%10
    if c3==c1:
        return True
    else:
        return False

