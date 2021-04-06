
def combinations(k, n):
    def fact(i):
        if i < 1:
            return 1
        return fact(i-1)*i
    return (fact(n)/(fact(k)*fact(n-k)))

