
def anti_divisors(n):
    lst = []
    for i in range(1,n+1):
        if n%i!=0:
            if i%2!=0 and (((n*2)-1)%i==0 or ((n*2)+1)%i==0):
                lst.append(i)
            elif (n*2)%i==0:
                lst.append(i)
    return lst

