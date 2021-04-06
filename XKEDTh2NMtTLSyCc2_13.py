
def valid_credit_card(number):
    a,b=[],[]
    for i in str(number)[-2::-2]:
        a.append(int(i)*2)
    for i in range(len(a)):
        if a[i] > 9:
            a[i]=int(str(a[i])[0])+int(str(a[i])[1])
    for i in str(number)[::-2]:
        b.append(int(i))
    if (sum(a)+sum(b))%10==0:
        return True
    else:
        return False

