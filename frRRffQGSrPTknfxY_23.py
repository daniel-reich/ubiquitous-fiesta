
def digit_count(n):
    return int(''.join([str(str(n).count(c)) for c in str(n)]))

