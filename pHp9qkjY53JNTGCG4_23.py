
def century_from_year(n):
    if n % 100 == 0:
        return n // 100
    else:
        return n // 100 + 1

