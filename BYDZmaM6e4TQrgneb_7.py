
def fib_fast(num):
    fib = [0,1]
    for i in range(num-1):
        new = fib[-1]+fib[-2]
        fib.append(new)
        
    return fib[num]

