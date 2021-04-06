
def multiply_by_11(n):
    n1='0'+n
    n2=n+'0'
    ans=''
    c=0
    for i in range(len(n1)-1,-1,-1):
        s=int(n1[i])+int(n2[i])+c
        ans+=str(s%10)
        c=1*(s>=10)
    return (str(c)+ans[::-1]).lstrip('0')

