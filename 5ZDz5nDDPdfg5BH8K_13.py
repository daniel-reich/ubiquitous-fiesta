
def only_5_and_3(n):
    if n in [3, 5]:
        return True
    if n <= 0:
        return False
    return only_5_and_3(n - 5) or only_5_and_3(n / 3)

