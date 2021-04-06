
def collatz(n: int) -> list:
    if n == 1:
        return [0, 1]
    seq, counter = [], 0
    while n > 1:
        if n % 2 != 0:
            n = n * 3 + 1
            seq.append(n)
        else:
            n //= 2
            seq.append(n)
        counter += 1
    return [counter, max(seq)]

