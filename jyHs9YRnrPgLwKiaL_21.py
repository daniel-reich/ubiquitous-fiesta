
def split(x):
    return round(max((x / i) ** i for i in range(2, x)), 1) if x > 1 else 1

