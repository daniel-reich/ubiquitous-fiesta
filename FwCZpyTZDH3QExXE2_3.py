
def amount_fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        t = [0,1,1]
        while n > t[len(t)-1]:
            t.append((t[len(t)-1] + t[len(t)-2]))
        return len(t)-1

