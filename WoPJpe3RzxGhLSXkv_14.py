
def concatenation_sum(n):
    if len(str(n)) == 1:
        return n
    else:
        return (n - 10 ** (len(str(n)) - 1) + 1) * (len(str(n))) + concatenation_sum(10 ** (len(str(n)) - 1) -1)

