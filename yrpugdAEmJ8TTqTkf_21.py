
def secret(num):
    d, r = divmod(num, 10)
    return pow(d, r) - d * r

