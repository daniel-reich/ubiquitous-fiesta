
def collatz(n):
    m = [n]
    while n != 1:
        if n%2==0:
            n = n/2
            m.append(int(n))
        else:
            n = n*3 + 1
            m.append(int(n))
    return (len(m),max(m))

