
def collatz(n):
    l = [n]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        l.append(n)
    return [len(l)-1,max(l)]

