
def digits_count(num):
    counter = 1
    if abs(num) < 10:
        return counter
    num //= 10
    return digits_count(num) + counter

