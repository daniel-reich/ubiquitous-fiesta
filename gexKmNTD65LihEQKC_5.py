
def is_super_cool(string):
    dic={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
         8:'eight',9:'nine',10:'ten',11:'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
         15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
         19 : 'nineteen', 20 : 'twenty',30 : 'thirty', 40 : 'forty'}
    n=len(string)
    if n==0:
        return False
    while n:
        if n<=20:
            a=dic[n]
        if (21<n< 100):
            if n% 10 == 0:                
                a=dic[n]
            else:
                a=dic[n//10 * 10]+dic[n%10]
        if len(a)==n:
            return True
            break
        else:
            n=len(a)
    return False

