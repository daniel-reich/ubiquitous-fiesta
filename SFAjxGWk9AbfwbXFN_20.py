
def primes_below_num(n):
    result=[]
    for x in range (2,n+1):
        if x>1:
            for y in range (2,x):
                if x%y==0:break
            else: result=result+[x]   
    return result

