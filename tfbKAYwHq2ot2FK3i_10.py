
def non_repeats(radix):
    def p(n, k):
        result = 1
        for j in range(n-k+1, n+1):
            result *= j
        return result
​
    total = radix - 1
    for i in range(2, radix+1):
        total += (p(radix, i) - p(radix-1, i-1))
    return total

