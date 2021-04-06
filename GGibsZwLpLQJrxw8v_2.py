
def get_lucky_number(size, nth):
    lst = list(range(1, size + 1))
    sieve_filter = [1]
    for step in range(2, nth + 1):
        i = 0
        while lst[i] in sieve_filter:
            i += 1
        sieve_filter.append(lst[i])
        lst = [val for k, val in enumerate(lst) if (k + 1) % sieve_filter[-1]]
    return lst[nth - 1]

