
def simplify(txt):
    temp1=""
    temp2=""
    index=txt.find('/')
    for i in range(0,index):
        temp1+=txt[i]
    for i in range(index+1,len(txt)):
        temp2+=txt[i]
    num1=int(temp1)
    num2=int(temp2)
    gcd=1
    for i in range(1,min(num1,num2)+1):
        if(num1%i==0 and num2%i==0):
            gcd=i
    if(num2//gcd==1):
        return str(num1//gcd)
    else:
        return str(num1//gcd)+'/'+str(num2//gcd)

