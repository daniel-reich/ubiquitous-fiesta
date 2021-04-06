
def get_lucky_number(size, nth):
    lst = [i for i in range(1, size+1)]
    sieve = 2
    pos = 0
    while len(lst) >= sieve:
        lst = [lst[i] for i in range(len(lst)) if not (i+1) % sieve == 0]
        sieve = lst[pos+1]
        pos += 1
    return lst[nth-1]

