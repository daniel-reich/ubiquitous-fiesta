
def is_harshad(n):
    a = sum([int(x) for x in str(n)])
    return n%a == 0

