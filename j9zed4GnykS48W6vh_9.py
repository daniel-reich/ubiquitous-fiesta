
def digits(number):
    exponent = len(str(number)) - 1
    number = number - (10**exponent)
    return base(exponent) + number*(exponent+1)
​
def base(size):
    return (10**size - 10**(size-1)) * size + base(size-1) if size > 0 else 0

