
def repeating_cycle(n):
    gen, memo, current, index = decimals(n), "", "", 0
    next(gen)
    for _ in range(20000):
        a, b = next(gen), next(gen)
        current += a + b
        memo += current[index]
        index += 1
        if 2 * memo == current and len(set(memo)) > 1:
            return index
    return -1
​
def decimals(num):
    dividend = 1
    while dividend:
        yield str(dividend // num)
        dividend = dividend % num * 10

