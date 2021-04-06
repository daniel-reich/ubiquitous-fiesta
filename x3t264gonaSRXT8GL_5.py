
def repeating_cycle(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    remnants = []
    rem = 1
    while True:
        rem = (10 * rem) % n
        if rem == 0:
            return -1
        if rem in remnants:
            return len(remnants) if rem == remnants[0] else -1
        remnants.append(rem)

