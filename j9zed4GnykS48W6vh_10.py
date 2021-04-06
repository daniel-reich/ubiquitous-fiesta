
def digits(num):
    x = len(str(num)) - 1
    digits_ = x * pow(10, x) + (1 - pow(10, x)) // 9
    rest_digits = (num - 10 ** x) * len(str(pow(10, x)))
    return digits_ + rest_digits

