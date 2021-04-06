
def fib_fast(num):
    fn = 0
    fn1 = 1
    for i in range(0, num):
        oldFn = fn
        fn = fn1 + fn
        fn1 = oldFn
    return fn
​
print(fib_fast(50))

