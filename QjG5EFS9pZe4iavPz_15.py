
def fib(n):
    if n==0:
        return 0
    
    
    elif n>2:
        nex_number=1
        prev_number=1
        container=0
        for i in range(1,n-1):
            container=nex_number
            nex_number=nex_number+prev_number
            prev_number=container
            print(nex_number)
​
        return nex_number
​
    else:
        return 1

