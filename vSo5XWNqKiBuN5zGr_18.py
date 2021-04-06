
def divide(dividend, divisor):
    neg = 1
    if dividend < 0 and divisor < 0:
        dividend *= -1
        divisor *= -1
    elif dividend < 0 or divisor <0:
        neg = -1
        if dividend < 0:
            dividend *= -1
        else:
            divisor *= -1
    if dividend < divisor:
        return 0
    return neg*(1 + divide(dividend-divisor, divisor))

