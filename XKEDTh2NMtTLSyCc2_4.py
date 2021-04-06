
def valid_credit_card(number):
    text=list(str(number))
​
    for i in range(len(text)-2,-1,-2):
        t=int(text[i])*2
        if(t>9):
            t=t-9
        text[i]=t
    sum=0
    for i in range(len(text)):
        sum=sum+int(text[i])
​
​
    if(sum%10==0):
        return True
    else:
        return False

