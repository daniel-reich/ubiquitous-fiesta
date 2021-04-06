
def chocolates_parcel(n_small, n_big, order):
    if order in (1,3):
        return -1
​
    n5=(order//10)*2
    if order%2==1:
        if  n5*5+5<=order:
            n5+=1
        else:
            n5-=1
    n2=(order-n5*5)/2
    while n5>n_big:
        n5-=2
        n2+=5
    if n2<=n_small  and n5>=0:
        return n2
    else:
        return -1

