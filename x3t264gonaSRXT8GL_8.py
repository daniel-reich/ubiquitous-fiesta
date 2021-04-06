
def repeating_cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    remainders = []
    rem = 1
    while True:
        rem = (10 * rem) % n
        if rem == 0:
            return -1
        if rem in remainders:
            return len(remainders) if rem == remainders[0] else -1
        remainders.append(rem)

