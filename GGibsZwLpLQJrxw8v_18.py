
def get_lucky_number(size, nth):
    l = list(range(1, size + 1))
    sieve_filter = 2
    while len(l) >= sieve_filter:
        l = [n for i, n in enumerate(l) if (i + 1) % sieve_filter]
        for n in l:
            if n > sieve_filter:
                sieve_filter = n
                break
    return l[nth - 1]

