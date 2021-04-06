
def palindrome_descendant(num):
    if  str(num)==str(num)[::-1]:
        return True
    while num>9:
        num=str(num)
        t=''
        for i in range(0,len(num),2):
            t+=str(int(num[i])+int(num[i+1]))
        if len(t)%2==1:
            return False
        if  t==t[::-1]:
            return True
        num=int(t)
    return False

