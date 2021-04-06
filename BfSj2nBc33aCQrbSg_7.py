
def truncatable(n):
    n = str(n)
    if('0' in n):return False
    left = sum(list(1 for i in range(len(n)) if isPrime(int(n[i:]))))
    right = sum(list(1 for j in range(1,len(n)+1) if isPrime(int(n[:j]))))
    if (left==len(n)==right):return 'both'
    if (left==len(n)!=right):return 'left'
    if (left!=len(n)==right):return 'right'
    return False
    
​
​
def isPrime(x):
    if(x<2):return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
​
    return True

