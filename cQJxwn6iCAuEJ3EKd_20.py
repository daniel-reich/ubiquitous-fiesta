
def digits_count(n):
    return 1 if abs(n) < 10 else digits_count(n//10) + 1

