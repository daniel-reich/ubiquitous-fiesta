
def moran(n):
    s = sum(list(map(lambda x:int(x),list(str(n)))))
    def isprime(n):
        for i in range(2, n - 1):
            if n % i == 0:
                return False
        return True
    return 'M' if n%s==0 and isprime(n//s) else 'H' if n%s==0 else 'Neither'

