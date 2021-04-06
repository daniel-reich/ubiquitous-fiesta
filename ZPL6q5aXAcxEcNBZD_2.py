
def funny_numbers(n, p):
    s = sum(pow(int(d), i + p) for i, d in enumerate(str(n)))
    return None if s % n else s // n

