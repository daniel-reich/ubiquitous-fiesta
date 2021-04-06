
def happy(n):
    while n!=1 and n!=4: 
        n=sum(int(i)**2 for i in str(n))
    return n==1

