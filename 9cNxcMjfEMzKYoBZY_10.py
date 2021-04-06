
def num_type(n):
    sum1=0
    sum2=0
    for i in range(1,n):
        if n%i==0:
            sum1+=i
    print(sum1)
    if sum1==n:
        return "Perfect"
    elif sum1!=n:
        for i in range(1,sum1):
            if sum1%i==0:
                sum2+=i
    if sum2==n:
        return "Amicable"
    else:
        return "Neither"

