
fib = [0, 1]
a, b = 0, 1
for _ in range(100):
    a, b = b, a + b
    fib.append(b)
    
def fib_fast(num):
    return fib[num]

