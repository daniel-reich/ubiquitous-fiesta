
def little_big(n):
    if n %  2 == 1:
        return 5 + (n // 2)
    return (2**((n // 2) -1)) * 100

