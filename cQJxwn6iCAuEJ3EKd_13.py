
def digits_count(num, begin=1):
    return digits_count(int(num / 10), 0) + 1 if num else begin

