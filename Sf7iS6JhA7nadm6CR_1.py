
def divisibility_rule(n):
    seq = [1, 10, 9, 12, 3, 4]
    seen = set([n])
    while True:
        digits = [int(_) for _ in str(n)[::-1]]
        n = 0
        for k in range(len(digits)):
            n += digits[k] * seq[k % len(seq)]
        if n in seen:
            return n
        seen.add(n)

