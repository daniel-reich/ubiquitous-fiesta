
def is_exact(num):
    n = num
    i = 2
    
    def factorials(n, i):
        print(n, i)
        if n == i:
            return [num, i]
        if n % i == 0:
            return factorials(int(n/i), i+1)
        else:
            return "Not exact!"
    return factorials(n, i)

