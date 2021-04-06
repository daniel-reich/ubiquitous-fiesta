
def amount_fib(n):
    i = 0
    cnt = 0
    while True:
        x = fibFast(i)
        if x >= n:
            break
        i += 1
        cnt += 1
    return cnt
​
def fibFast(num):
    if num == 0:
        return 0
    a = 0
    b = 1
    for x in range(num-1):
        a, b = b, a+b
    return b

