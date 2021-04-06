
def prime_numbers(num):
    a = [p for p in range(2,num) if 0 not in [p%d for d in range(2,p)]]
    return len(a)

