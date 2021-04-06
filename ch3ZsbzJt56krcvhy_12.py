
def square_root(n):
    est = int(n**0.5)
    while True:
        est = int((est + n//est)//2)
        if est * est == n:
            return est

