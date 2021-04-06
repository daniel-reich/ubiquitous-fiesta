
def anti_divisors(n):
    double, divisors = n*2, []
    double_high, double_low = n*2 + 1, n*2 - 1
​
    for i in range(2, n):
        if n%i:
            if i%2 and (not double_high%i or not double_low%i):
                divisors.append(i)
            elif not i%2 and not double%i:
                divisors.append(i)
    return divisors

