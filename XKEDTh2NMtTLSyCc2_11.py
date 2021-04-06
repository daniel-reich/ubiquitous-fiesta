
def digits(n):
    return [int(i)for i in str(n)]
def valid_credit_card(number):
    x=digits(number)
    y=x[-1::-2]
    z=x[-2::-2]
    count=0
    count+=sum(y)
    for i in z:
        count+=sum(digits(i*2))
    a=count%10
    print(a)
    return a==0

