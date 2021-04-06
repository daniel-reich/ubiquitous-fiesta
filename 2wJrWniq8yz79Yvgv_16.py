
def is_narcissistic(n):
    return sum(int(i)**len(str(n)) if len(str(n))>1 else int(i) for i in str(n))==n

