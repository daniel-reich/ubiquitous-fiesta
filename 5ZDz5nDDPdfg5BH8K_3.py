
def only_5_and_3(n):
    if n < 3: return False
    if n == 3: return True
    if n % 5 == 0: return True
    return only_5_and_3(n / 3) or only_5_and_3(n - 5)

