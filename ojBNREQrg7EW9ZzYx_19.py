
import math
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    m=total_money
    a,b='',''
    c=cost_of_one_chocolate
    for i in m:
        if i.isnumeric():
            a+=str(i)
    for i in c:
        if i.isnumeric():
            b+=str(i)
        if '-' in i:
            b+='-'    
    if int(a)<=0 or int(b)<=0:
        return "Invalid Input"
    else:
        n=(int(a)//int(b))
        count=n
        while n:
            n=n-2
            count+=1
            if n<=0:
                return count-1

