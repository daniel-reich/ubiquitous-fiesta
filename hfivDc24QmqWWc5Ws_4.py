
def eratosthenes(num) :
    return [n for n in range(2, num+1) if all(n%x for x in range(2,n))]

