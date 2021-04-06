
def check_perfect(x):
    lst=[]
    for i in range(1,x):
        if (x%i==0):
            lst.append(i)
    sum=0  
    for i in lst:
        sum +=i
       
    return sum==x

