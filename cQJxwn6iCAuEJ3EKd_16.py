
def digits_count(num):
    if abs(num) < 10:
        return 1
    return digits_count(abs(num) // 10) + 1

