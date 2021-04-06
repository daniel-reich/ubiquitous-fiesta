
def trailing_zeros(n):
    count, power = 0, 1
    divisor = pow(5, power)
    while divisor <= n:
        count += n // divisor
        power += 1
        divisor = pow(5, power)
    return count

