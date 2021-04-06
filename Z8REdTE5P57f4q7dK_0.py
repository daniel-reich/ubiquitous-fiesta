
def collatz(n):
    res = []
    while n != 1:
        res.append(n)
        n = n*3 + 1 if n%2 else n//2
    return len(res) + 1, max(res)

