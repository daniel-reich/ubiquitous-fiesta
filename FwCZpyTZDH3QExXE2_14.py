
def amount_fib(n):
    x,y, cnt = 0,1,0
    while x<n:  x,y,cnt = y, x+y, cnt+1
    return cnt

