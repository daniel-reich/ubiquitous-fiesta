
def is_narcissistic(n):
    power = len(str(n))
    total = sum([int(num)**power for num in str(n)])
    if n == total:
        return True
    return False

