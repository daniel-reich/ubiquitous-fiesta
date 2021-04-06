
def kempner(num):
    if num ==1:
        return 1
    def factorial(n):
        fac = 1
        for l in range(1,n+1):
            fac *= l
        return fac
    for i in range(2,num+1):
        if factorial(i)%num == 0:
            return i

