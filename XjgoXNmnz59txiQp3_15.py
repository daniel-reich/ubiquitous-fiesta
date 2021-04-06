
def split(n):
    return n if n < 5 else 3*split(n-3)

